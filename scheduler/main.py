from function import *

def input_menu():
	while True:
		number = input()
		if not number.isnumeric():
			print('Не верный ввод данных. Введите цифру от 1 до 6: ')
		elif not (1 <= int(number) <=6):
			print('Не верный ввод данных. Введите цифру от 1 до 6: ')
		else:
			return(int(number))

number = 0
clear = '\n' * 100
while (number != 6):
	#print(clear)
	print('Ежедневник. Выберите действие: \n\n 1. Вывести список задач \n 2. Добавить задачу \n 3. Отредактировать задачу \n 4. Завершить задачу \n 5. Начать задачу с начала \n 6. Завершить задачу \n')
	number = input_menu()
	if (number == 1) : 
		print_scheduler()
	elif (number == 2) : add_scheduler()
	elif (number == 3) : edit_scheduler()
	elif (number == 4) : end_scheduler()
	elif (number == 5) : begin_again_scheduler()

 	


