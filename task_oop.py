import json
"""
Сделать класс с методами
Каждый файл это объект. и работать внутри объекта методами и свойствами.
Как мысль можно отдельно создать под каждый тип файла отдельный модуль с каким то специальннымы расширением. В этом модуле уже будут поведение и свойства именного этого типа файла.
И отдельный модуль который считывает по заданноымм параметрам эти файлы и создает списко этих классов.
После уже в главный модель передать эту библитотеку в наш класс через свойство и уже работать. 
Мне кажется так будет более гибкая система под добавление новых типов файлов.
Выйдет Класс в классе с подклассом
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
