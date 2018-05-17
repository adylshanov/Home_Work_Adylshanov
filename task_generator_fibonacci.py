# -*- coding: utf-8 -*-


def fibonacci(n):
    a = 0
    rez = b = 1
    for i in range(n):
        yield rez
        rez = a + b
        a, b = b, rez

if __name__ == '__main__':
    for i in fibonacci(10):
        print(i)
