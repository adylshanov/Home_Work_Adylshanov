'''
Модуль перевода в разные системы исчисления
'''
__all__ = [
	'dec2bin',
	'dec2oct',
	'dec2hex',
	'bin2dec',
	'oct2dec',
	'hex2dec'
]

def dec2bin(number):
	"""Переводит из десятиричной системы в двоичную"""
	return code(number, 2)

def dec2oct(number):
	"""Переводит из десятиричной системы в восьмеричную"""
	return code(number, 8)

def dec2hex(number):
	"""Переводит из десятиричной системы в шестнадцатиричную"""
	return code(number, 16)


def code(number, sysnum):
	""" Функция перевода десятичного числа в sysnum систему исчисления """
	rez = ''
	while (number >= 1):
		if (number%sysnum >= 10):
			rez = ifinhex(number%sysnum) + rez
		else :
			rez = str(number%sysnum) + rez
		number = number//sysnum
	return str(rez)


def bin2dec(number):
	"""Переводит из двоичной системы в десятиричную"""
	return decode(number, 2)

def oct2dec(number):
	"""Переводит из восьмеричной системы в десятиричную"""
	return decode(number, 8)

def hex2dec(number):
	"""Переводит из шестнадцатеричную системы в десятиричную"""
	return decode(number, 16)

def decode(number, sysnum):
	""" Функция перевода числа из sysnum систем исчисления в десятиричную """
	tx = str(number)
	tx = tx[::-1]
	rez = 0
	for i in range(len(tx)):
		if tx[i].isalpha() == True:
			rez += int(ifouthex(tx[i])) * (sysnum ** (i))
		else :
			rez += int(tx[i]) * (sysnum ** (i))
	return int(rez)

def ifouthex(char):
	""" замена буквы на число в системе исчисления больше десятичной """
	if char == 'a':
		return 10
	elif char == 'b':
		return 11
	elif char == 'c':
		return 12
	elif char == 'd':
		return 13
	elif char == 'e':
		return 14
	elif char == 'f':
		return 15

def ifinhex(char):
	""" вставка символа буквы в систему исчисления больше десятичной """
	if char == 10 :
		return 'a'
	elif char == 11:
		return 'b'
	elif char == 12:
		return 'c'
	elif char == 13:
		return 'd'
	elif char == 14:
		return 'e'
	elif char == 15:
		return 'f'

if __name__ == '__main__' :
	print(dec2bin(250))
	print(dec2oct(493))
	print(dec2hex(11259375))
	print(bin2dec(dec2bin(250)))
	print(oct2dec(dec2oct(493)))
	print(hex2dec(dec2hex(11259375)))
