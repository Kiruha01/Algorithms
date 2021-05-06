# LSD sort
[![Python application](https://github.com/Kiruha01/Algorithms/actions/workflows/python-app.yml/badge.svg)](https://github.com/Kiruha01/Algorithms/actions/workflows/python-app.yml)

Поразрядная сортировка слов, состоящие из букв `a-z`.

### input.txt
В первой строке входного файла (input.txt) содержится 
* число `N` — число строк,
* число `M` — их длина, 
* число `K` – число фаз цифровой сортировки

Далее по вертикали записаны строки, то есть вторая строка файла состоит из первых символов N строк, 
третья строка файла состоит из вторых символов N строк и т.д.

###### Пример
Строки 
```
aab
bab
bbb
```
Образуют слова `abb` (1 столбец), `aab` (2 столбец), `bbb` (3 столбец).

### output.txt
Необходимо вывести номера строк в порядке после K фаз цифровой сортировки по младшему разряду 
(*LCD*-сортировка, **Least Significant Digit radix sort**).