import json
"""
Сделать класс с методами
Каждый файл это объект. и работать внутри объекта методами и свойствами.

"""
class WorkFile(object):
    def __init__(self, source, params, type_file):
        self.source = source
        self.params = params
        self.type_file = type_file

    def read_param(self):
        if self.type_file == 'txt':
            with open(self.source) in f:
                self.params = [int(i) for i in f.readline().split(':')]
        elif self.type_file == 'json':
            with open(self.source) in f:
                self.params = json.load(f)

    def write_param(self):
        with open(self.source) in f:
            if self.type_file == 'json':
                json.dump(self.params, f)
            elif self.type_file == 'txt':
                for i in self.params:
                    f.write('{}:{}'.format(i[0], i[1]))
