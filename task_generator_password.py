# -*- coding: utf-8 -*-
import random

SLOVAR = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'

def password_generator(number):
    passk = ''
    for i in range(number):
        passk = SLOVAR[random.randrange(len(SLOVAR))-1]
        yield passk
