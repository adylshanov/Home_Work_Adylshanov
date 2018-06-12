class OneLink(object):
	"""один элемент с сылкой на последующий"""
	def __init__(self, value, link_next):
		self.value = value
		self.link_next = link_next

	def set_next(self, next):
		self.link_next = next


class LinkedList(object):
	def __init__(self, *values):
		self.begin = None
		self.last = None
		self.size = 0
		self.it = 0

		for i in values:
			self.add(i)

	def add(self, value):
		"""Добавление в конец элемента"""
		if self.size == 0:
			self.begin = self.last = OneLink(value, None)
		else:
			self.last.link_next = self.last = OneLink(value, None)
		self.size += 1
		#print('len {}'.format(self.size))

	def __str__(self):
		"""перегрузка для вывода списка"""
		i = self.begin
		if i != None:
			s = str(i.value) + ' '
			while i.link_next != None:
				i = i.link_next
				s += str(i.value) + ' '
				#print(str(i.value), str(i.link_next))
		else: s = ''
		return s

	def insert(self, index, value):
		"""добавляет элемент в указаную позицию"""
		if index >= self.size:
			self.add(value)
			return
		elif index == 0:
			self.begin = OneLink(value, self.begin)
		else:
			i = self.begin
			step = 1
			while i.link_next != None:
				if step == index:
					i.link_next = OneLink(value, i.link_next)
					break
				i = i.link_next
				step += 1
		self.size += 1

	def get(self, index):
		""" возращает значение с указаным индексом"""
		#print(index, self.size)
		if index >= self.size:
			raise IndexError
		
		if index+1 == self.size:
			return self.last.value

		i = self.begin
		step = 0	
		while i.link_next != None:
			if step == index:
				#print(str(i.value))
				return i.value
			step += 1
			i = i.link_next

	def remove(self, value):
		"""удаление заданого с указаным значеним"""
		d = i = self.begin
		while i != None:
			if i.value == value:
				self.size -= 1
				if i.link_next == None:
					d.link_next = None
				else:
					i.value = i.link_next.value
					i.link_next = i.link_next.link_next
				break
			d = i
			i = i.link_next
		

	def remove_at(self, index):
		if index >= self.size: raise IndexError

		d = self.begin
		i = d.link_next
		step = 0
		while i.link_next != None:
			if step == index:
				if i.link_next == None:
					d.link_next = None
				else:
					temp = i.value
					i.value = i.link_next.value
					i.link_next = i.link_next.link_next
				self.size -= 1
				#print(self.size)
				return temp
			step += 1
			d = i
			i = i.link_next

	def clear(self):
		self.__init__()

	def contains(self, value):
		i = self.begin
		while i != None:
			if i.value == value:
				return True
			i = i.link_next
		return False

	def len(self):
		return self.size

	def is_empty(self):
		if self.begin == None:
			return True
		else: return False

	def __iter__(self):
		return self

	def __next__(self):
		#if self.it == 0:
			#i = self.begin
			#self.it = 1
			#return i.value
		if self.it == self.size: 
			raise StopIteration
		else:
			self.it += 1
			#print(self.it)
			return self.get(self.it-1)




if __name__ == '__main__':
	l1 = LinkedList(1, 2, 3, 4, 5)
	#print(l1.len())
	#print(l1)
	l1.add(6)
	#print(l1)
	l1.insert(0,10)
	print(l1)
	l1.insert(2,20)
	print(l1)
	l1.insert(8,30)
	print(l1)
	#print(l1.len())
	#print(l1.get(1))
	#print(l1.get(8))
	#l1.remove(2)
	#print(l1)
	#l1.remote_at(0)
	#l1.remote_at(100)
	#print(l1)
	#l1.clear()
	#print(l1)
	#print(l1.contains(3))
	#print(l1.contains(100))
	print(l1.len())
	#print(l1.is_empty())
	"""
	l2 = LinkedList('item1', 'item2', 'item3')
	print(l2.get(3))
	print(l2)
	for item in l2: print(item)
	"""

