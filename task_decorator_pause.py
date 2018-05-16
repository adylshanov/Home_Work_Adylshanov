# -*- coding: utf-8 -*-
import time

def pause(t):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(t)
            return func()
        return wrapper
    return decorator

@pause(2)
def func():
    print('Функиця выполняется с задержкой в 2 секунд')


if __name__ == '__main__' :
    func()
    func()
