# -*- coding: utf-8 -*-
from collections import namedtuple

def return_namedtuple(*names):
    def decorator(func):
        #name
        def wrapper(*args, **kwargs):
            Func = func(*args, **kwargs)
            if isinstance(func(*args, **kwargs), tuple):
                #print(names)
                #print(func(*args, **kwargs))
                rez = namedtuple(func.__name__, names)
                return rez(*Func)
            return Func
        return wrapper
    return decorator

@return_namedtuple('one', 'two')
def func():
    return 1, 2

if __name__ == '__main__':
    r = func()
    print(r.one) # 1
    #print(r.two) # 2
