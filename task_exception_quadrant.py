# -*- coding: utf-8 -*-

def get_quadrant_number(x, y):
    """Возращает номер четверти"""
    if (x > 0): #and (y > 0):
        if (y > 0):
            return 1
        elif (y < 0):
            return 4
        else:
            raise ValueError()
    elif (x < 0): #and (y > 0):
        if (y > 0):
            return 2
        elif (y < 0):
            return 3
        else:
            raise ValueError()
    else:
        raise ValueError()

if __name__ == '__main__':
    print(get_quadrant_number(1, 1))
    print(get_quadrant_number(-1, 1))
    print(get_quadrant_number(-1, -1))
    print(get_quadrant_number(1, -1))
    #print(get_quadrant_number(1, 0))
    print(get_quadrant_number(0, 0))
