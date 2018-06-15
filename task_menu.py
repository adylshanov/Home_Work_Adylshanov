from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
	"""docstring for Command"""
	def __init__(self, arg):
		super(Command, self).__init__()
		self.arg = arg

	def execute():
		pass
		