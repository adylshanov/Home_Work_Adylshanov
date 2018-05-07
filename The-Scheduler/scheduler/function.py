#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as Path
import sys
import sqlite3
from datetime import datetime

SQL_SELECT_TASK = '''
	SELECT
	id_task, name_task,	test_task, date_create, date_end, date_close,
	(SELECT status_name FROM status WHERE status_task = status.id_task)
	FROM task
'''
SQL_INSERT = 'INSERT INTO task (name_task,test_task,date_end) VALUES ((?), (?), (?))'


SQL_SELECT_STATUS_TASK ='''
	SELECT
	id_task, status_name
	FROM status
	'''

SQL_UPDATE = '''
	UPDATE task
	SET {}='{}'
	WHERE id_task={}
	'''

get_conn = lambda: connect('scheduler.sqlite')

def connect(db_name = None):
	if db_name is None:
		db_name = ':memory:'
	conn = sqlite3.connect(db_name)
	return conn

def initialize(conn):
	script_path = Path.join(Path.dirname(__file__),'schema.sql')

	with conn, open(script_path) as f:
		conn.executescript(f.read())

def print_scheduler():
	"""Вывод списка задач"""
	print('Список всех задач')
	conn = get_conn()
	with conn:
		cursor = conn.cursor()
		cursor.execute(SQL_SELECT_TASK)
		while 1:
			row = cursor.fetchone()
			if row == None:
				break
			print (str(row[0]).rstrip(),')',row[1],'\n',row[2])
			if row[5] != None :
				print('Дата завершения:', row[5],'Статус',row[6] )
			else:
				print('Планируемая дата завершения:', row[4],'Статус',row[6])

def add_scheduler():
	"""добавление задачи"""
	conn = get_conn()
	task = input_task_add()
	with conn:
		cursor = conn.execute(SQL_INSERT,(task['1'],task['2'],task['4']))


def edit_scheduler():
	"""Редактирование задачи"""
	print_scheduler()
	conn = get_conn()
	index = int(input('Введите id задачи, которую нужно отредактировать\n'))
	param = show_menu_edit()
	update = input('Введите новые данные (если дата, то в формате ГГГГ-ММ-ДД): ')
	with conn:
		#print(SQL_UPDATE.format(param, str(update), index))
		cursor = conn.execute(SQL_UPDATE.format(param, str(update), index))
	pass

def end_scheduler():
	"""завершение задачи"""
	print_scheduler()
	conn = get_conn()
	index = int(input('Введите id задачи, которую нужно завершить\n'))
	param = 'date_close = CURRENT_DATE, status_task'
	#print(SQL_UPDATE.format(param, 1, index))
	with conn:
		cursor = conn.execute(SQL_UPDATE.format(param, 1, index))

def edit_status_task():
	"""Изменить статус задачи"""
	print_scheduler()
	conn = get_conn()
	index = int(input('Введите id задачи, статус которой нужно изменить\n'))
	print_status()
	while 1:
		cmd = input('\n     Введите статус:')
		if cmd:
			with conn:
				cursor = conn.execute(SQL_UPDATE.format('status_task', cmd, index))
				break
		else :
			print('Неизвестная программа')


def action_exit():
	"""выход из программы"""
	sys.exit(0)

def input_task_add():
	while 1:
		task = {
		'1': input('Введите название задачи:'),
		'2': input('Введите описание задачи:'),
		'4': input('Введите дату окончания (формат даты ГГГГ-ММ-ДД):') #не придумал способ проверки даты. чтобы просто и изящно.
	}
		return task

def show_menu_edit():
	print('\n Выберете какой параметр вы хотите изменить:\n 1. Изменить тему задачи \n2. Изменить описание задачи\n3. Изменить дату окочания задачи')
	actions = {
        '1': 'name_task',
        '2': 'test_task',
        '3': 'date_end',
    }
	while 1:
		cm = input()
		action = actions.get(cm)
		if action:
			return action
		else :
			print('Неизвестная программа')\

def print_status():
	conn = get_conn()
	with conn:
		cursor = conn.cursor()
		cursor.execute(SQL_SELECT_STATUS_TASK)
		while 1:
			row = cursor.fetchone()
			if row == None:
				break
			print(row[0],')',row[1])
