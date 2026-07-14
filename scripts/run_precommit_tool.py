#!/usr/bin/env python3
"""Run Python pre-commit tools with retries for transient Windows launch errors."""

from __future__ import annotations

import os
import runpy
import sys
import time
from collections.abc import Sequence
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from typing import NamedTuple

MAX_ATTEMPTS = 8
TRANSIENT_RETURN_CODES = {-1, 3221225477, 3221225501, 4294967295}
TRANSIENT_WINDOWS_ERRORS = ("[WinError 5]", "PermissionError")


class ToolResult(NamedTuple):
    """Captured result from a Python tool module."""

    returncode: int
    stderr: str
    stdout: str


def has_transient_windows_error(output: str) -> bool:
    """Return True when a tool failed because Windows temporarily blocked a process."""
    return sys.platform == "win32" and any(
        error in output for error in TRANSIENT_WINDOWS_ERRORS
    )


def has_transient_windows_return_code(return_code: int) -> bool:
    """Return True for silent Windows process-launch failures."""
    return sys.platform == "win32" and return_code in TRANSIENT_RETURN_CODES


def exit_code(error: SystemExit) -> int:
    """Convert SystemExit code values to process-style integer codes."""
    if error.code is None:
        return 0
    if isinstance(error.code, int):
        return error.code
    return 1


def run_module(args: Sequence[str]) -> ToolResult:
    """Run the requested module with the current Python interpreter."""
    module, *module_args = args
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    os.environ.setdefault("PYTHONUTF8", "1")

    old_argv = sys.argv[:]
    stdout = StringIO()
    stderr = StringIO()
    try:
        sys.argv = [f"{sys.executable} -m {module}", *module_args]
        with redirect_stdout(stdout), redirect_stderr(stderr):
            try:
                runpy.run_module(module, run_name="__main__")
            except SystemExit as error:
                return ToolResult(
                    exit_code(error), stderr.getvalue(), stdout.getvalue()
                )
    finally:
        sys.argv = old_argv
    return ToolResult(0, stderr.getvalue(), stdout.getvalue())


def main(argv: Sequence[str] | None = None) -> int:
    """Run a Python module and retry only transient Windows permission failures."""
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: run_precommit_tool.py MODULE [ARGS ...]", file=sys.stderr)
        return 2

    last_output = ""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            result = run_module(args)
        except PermissionError as error:
            last_output = f"PermissionError: {error}"
            result = None
        else:
            last_output = f"{result.stdout}\n{result.stderr}"
            is_transient = has_transient_windows_error(
                last_output
            ) or has_transient_windows_return_code(result.returncode)
            if result.returncode == 0 or not is_transient:
                sys.stdout.write(result.stdout)
                sys.stderr.write(result.stderr)
                return result.returncode

        if attempt < MAX_ATTEMPTS:
            time.sleep(0.5 * attempt)

    print(last_output, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
