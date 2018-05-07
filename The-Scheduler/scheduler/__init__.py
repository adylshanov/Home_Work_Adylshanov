#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Ежедневник"""

# импорт модулей
from scheduler import function

#get_conn = lambda: function.connect('scheduler.sqlite')

def show_menu():
    print('''Ежедневник.

Выберите действие:
1. Вывести список задач
d. Добавить задачу
3. Изменить задачу
4. Завершить задачу
5. Изменить статус задачи
q. Закрыть программу
''')


def main():
    with function.get_conn() as conn:
        function.initialize(conn)

    actions = {
        "1": function.print_scheduler,
        '2': function.add_scheduler,
        '3': function.edit_scheduler,
        '4': function.end_scheduler,
        '5': function.edit_status_task,
        'q': function.action_exit,
    }

    while 1:
        print('\n'*100)
        show_menu()
        cmd = input('\n     Введите команду:')
        action = actions.get(cmd)
        if action:
            action()
            input('\n Нажмите Enter')
        else :
            print('Не известная программа')
'''
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
'''
