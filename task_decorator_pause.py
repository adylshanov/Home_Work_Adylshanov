# -*- coding: utf-8 -*-
from functools import wraps
import time

def pause(t):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(t)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@pause(2)
def func():
    print('Функиця выполняется с задержкой в 2 секунд')


if __name__ == '__main__' :
    func()
