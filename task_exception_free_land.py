# -*- coding: utf-8 -*-

def get_free_land(ogorod, grad):
    if ogorod[0] == 0:
        raise ValueError("Не задана площадь участка")
    if (grad[0] == 0) or (grad[1] == 0):
        raise ValueError("Не задана площадь грядки")
    if (ogorod[0] * 100 < grad[0] * grad[1]):
        raise ValueError("Размер грядки больше размера участка")

    return ogorod[0] * 100 % (grad[0] * grad[1])

if __name__ == '__main__':
    print(get_free_land((100, '1:1'), (15,25)))
    print(get_free_land((0, '1:1'), (15,25)))
    print(get_free_land((100, '1:1'), (5,0)))
    print(get_free_land((6, '3:2'), (40,28)))
