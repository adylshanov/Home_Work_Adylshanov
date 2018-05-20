# -*- coding: utf-8 -*-
from random import randrange

SLOVAR = list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')

def password_generator(number):
    l = len(SLOVAR)
    while 1:
        rez = []
        #print(SLOVAR[random.randrange(len(SLOVAR))])
        for i in range(number):
            rez.append(SLOVAR[randrange(l)])
        yield ''.join(rez)

if __name__ == '__main__':
    gen = password_generator(10)
    print(next(gen))
