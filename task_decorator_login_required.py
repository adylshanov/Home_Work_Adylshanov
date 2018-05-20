# -*- coding: utf-8 -*-
from functools import wraps
import hashlib

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def initialize(username, password):
    s = username + password
    with open('token.txt', 'w') as f:
        f.write(hashlib.md5(s.encode()).hexdigest())

def login_required(func):
    memory = []
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'Accept' in  memory:
            return func(*args, **kwargs)
        #чтение логина\пароля из файла
        with open('token.txt', 'r') as f:
            token_file= f.read

        for i in range(3):
            login = input('Login: ')
            pass_login = input('Password: ')
            token_input = make_token(login, pass_login)
            print(token_input)
            if token_file == token_input:
                memory.append('Accept')
                break
            if i == 3 :
                return None
        return func(*args, **kwargs)
    return wrapper

@login_required
def f1():
    print('Функция защищена паролем')


@login_required
def f2():
    print('Эта функция тоже защищена паролем')


if __name__ == '__main__':
    initialize('Test', '123')
    f1()
