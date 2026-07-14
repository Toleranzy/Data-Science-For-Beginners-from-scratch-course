#!/usr/bin/env python3
"""Run Python pre-commit tools with retries for transient Windows launch
errors."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from collections.abc import Sequence
from typing import NamedTuple

MAX_ATTEMPTS = 12
TRANSIENT_RETURN_CODES = {-1, 3221225477, 3221225501, 4294967295}
TRANSIENT_WINDOWS_ERRORS = ("[WinError 5]", "PermissionError")


class ToolResult(NamedTuple):
    """Captured result from a Python tool module."""

    returncode: int
    stderr: str
    stdout: str


def has_transient_windows_error(output: str) -> bool:
    """Return True when a tool failed because Windows temporarily blocked a
    process."""
    return sys.platform == "win32" and any(
        error in output for error in TRANSIENT_WINDOWS_ERRORS
    )


def has_transient_windows_return_code(return_code: int) -> bool:
    """Return True for silent Windows process-launch failures."""
    return sys.platform == "win32" and return_code in TRANSIENT_RETURN_CODES


def run_module(args: Sequence[str]) -> ToolResult:
    """Run the requested module in a child process so crashes can be
    retried."""
    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("PYTHONUTF8", "1")
    result = subprocess.run(
        [sys.executable, "-m", *args],
        check=False,
        env=env,
        capture_output=True,
        text=True,
        errors="replace",
    )
    return ToolResult(result.returncode, result.stderr, result.stdout)


def main(argv: Sequence[str] | None = None) -> int:
    """Run a Python module and retry only transient Windows permission
    failures."""
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
