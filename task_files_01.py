# -*- coding: utf-8 -*-

n = int(input("Введите n:"))
p = int(input("Введите p:"))

with open('data.txt') as f:
    file = [int(i) for i in f.read().split()]

#1


with open('out-1.txt', 'w') as f:
    for i in file:
        if i%n == 0 :
            f.write(str(i)+' ')

#2
with open('out-2.txt', 'w') as f:
    for i in file:
        f.write(str(i**p)+' ')
