"""Ответы на вопросы по CPython и PyPy."""

# # [TASK] Cpython
#
# ## Введение в Python и CPython

# 1. Что такое CPython и чем он отличается от Python?
#
# ![Схема Python и CPython](python_sheme.png)
#
# 3. Сколько существует реализаций Python, и какая из них самая популярная?
#
# 6 реализаций. 'Cpython' самая популярная.
#
# 4. На каком языке написан CPython?
#
# 35% си. 65% python.
#
# Поиск и установка CPython
#
# 5. (опционально) Кто создал CPython?
#
# Guido van Rossum
#
# 6. Почему Python считается быстрым, несмотря на то, что это интерпретируемый язык?
#
# Потому что его ядро написано на си и вызывает инструкции из си.
#
# 7. Напишите путь к Интерпретатору CPython на вашем компьютере
#
# C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\python.exe
#
# Структура CPython
#
# Что содержится в папке include в CPython?
#
# Находятся файлы .h т.е. ядро Cpython.
#
# Где можно найти исходный код CPython дайте ссылку на репозиторий гитхаб
#
# https://github.com/python/cpython
#
# (опционально) Как работает интерпретатор CPython при выполнении кода?
# Запуск файла с помощью CPython
#
# 11. Какая команда используется для запуска файла с помощью CPython?
#
# python имя_файла.py
#
# 12. Можно ли запускать текстовые файлы через интерпретатор Python? Почему?
#
# Можно. Потому что их можно открыть с помощью интерпретатора.
#
# 13. Как указать путь к интерпретатору и файлу для выполнения кода?
#
# Расположение питона и там python.exe и есть интерпретатор. Файл создаешь в любой директории и просто после путя к интерпретатору подставляешь путь к файлу в cmd.
# \Users\User\AppData\Local\Python\pythoncore-3.14-64\python.exe C:\Users\User\Documents\GitHub\Data-Science-For-Beginners-from-scratch-course\python\text.txt
#
# Введение в PyPy
#
# 14. Чем PyPy отличается от CPython?
#
# PyPy быстрее Cpython в 10 раз.
#
# Почему PyPy не может использоваться для всех проектов на Python?
#
# Он новый и несовместим со всеми проектами на питоне.
#
# Где можно скачать PyPy?
#
# https://pypy.org/
#
# Установка и запуск PyPy
#
# 17. Как установить PyPy после скачивания?
#
# распаковать в папку архив PyPy
#
# 18. Как запустить файл с помощью PyPy?
#
# Сначала путь до pypy3.exe потом путь до файла. Это все в cmd
# \Users\User\programs\pypy3.11-v7.3.23-win64\pypy3.exe C:\Users\User\Documents\GitHub\Data-Science-For-Beginners-from-scratch-course\python\text.txt
#
# 19. Почему PyPy выполняет код быстрее, чем CPython?
#
# PyPy часто работает быстрее благодаря JIT-компилятору (Just-In-Time).
# Он отслеживает часто выполняемые участки программы, например циклы, и во время работы переводит их в машинный код процессора. Потом эти участки выполняются быстрее.
# CPython обычно исполняет байткод через свою виртуальную машину, поэтому на долгих вычислениях и циклах PyPy часто выигрывает по скорости.
#
# Практические задания
# Задание 1: Поиск и установка CPython
#
# установлен C:\Users\User\AppData\Local\Python\pythoncore-3.14-64
#
# Задание 2: Исследование структуры CPython
#
# C:\Users\User\AppData\Local\Microsoft\WindowsApps\python.exe
# C:\msys64\ucrt64\bin\python.exe
# C:\Users\User\AppData\Local\Python\bin\python.exe
#
# Откройте папку include и изучите её содержимое. Какое количество файлов на C там есть?
#
# 79 файлов.
#
# Перейдите на [GitHub-репозиторий CPython](https://github.com/python/cpython) и найдите файл README. Прочитайте информацию о проекте.
# прочитал
#
# Задание 3: Запуск файла с помощью CPython
#
# Создайте текстовый файл example.txt с содержимым:
# print("Hello from CPython!")
#
# Запустите файл через команду python <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
#
# python C:\Users\User\Documents\GitHub\Data-Science-For-Beginners-from-scratch-course\python\example.txt
#
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
#
# Ничего не поменялось
#
# Задание 4: Установка и использование PyPy
#
# Перейдите на [официальный сайт PyPy](https://www.pypy.org/) и скачайте подходящую версию для вашей операционной системы.
# Распакуйте скачанный архив в удобное место.
# Создайте файл example_pypy.py с кодом:
# print("Hello from pypy!")
#
# Запустите файл через PyPy
# pypy <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
#
# pypy3 "C:\Users\User\Documents\GitHub\Data-Science-For-Beginners-from-scratch-course\python\example_pypy.txt"
#
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
#
# Ничего не поменялось
#
# Задание 5: Сравнение производительности CPython и PyPy
#
# Execution time: 0.4358687400817871 seconds Cpython
#
# Execution time: 0.007019519805908203 seconds pypy3
#
# PyPy значительно быстрее Cpython
#
