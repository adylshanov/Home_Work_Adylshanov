# -*- coding: utf-8 -*-
import os
import json
import pickle
from abc import ABCMeta, abstractmethod

class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        passB

    @abstractmethod
    def write(self):
        pass


    types = {}
    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
    # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        #print(ext)
        #print(klass)
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        return klass(source, *args, **kwargs)

def add_type(type):
    def decorator(cls):
        ParamHandler.add_type(type, cls)
        return cls
    return decorator

@add_type('txt')
class TextParamHandler(ParamHandler):
    """  txt"""
    def read(self):
        with open(self.source) as f:
            self.params = [i for i in f.readline().split('=')]

    def write(self):
        with open(self.source, 'w') as f:
            for i in self.params:
                f.write('{}={}\n'.format(i,self.params[i]))

"""
@add_type('xml')
class XmlParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            self.params = [i for i in f.readline().split(':')]

    def write(self):
        with open(self.source, 'w') as f:
            for i in self.params:
                f.write('{}:{}\n'.format(i,self.params[i]))
"""

class ParamHandlerException(Exception):
    def __init__(self, ext):
        pass

@add_type('pickle')
class TextParamHandler(ParamHandler):
    """pickle"""
    def read(self):
        with open(self.source, 'rb') as f:
        	self.params = pickle.load(f)

    def write(self):
        with open(self.source, 'wb') as f:
        	pickle.dump(self.params, f)

@add_type('json')
class TextParamHandler(ParamHandler):
    """json"""
    def read(self):
        with open(self.source) as f:
        	self.params = json.load(f)

    def write(self):
        with open(self.source,  'w') as f:
        	json.dump(self.params, f, indent = 4)

if __name__ == '__main__':
    config = ParamHandler.get_instance('./params.pickle')
    config.add_param('key1', 'val1')
    config.add_param('key2', 'val2')
    config.add_param('key3', 'val3')
    config.write() # запись файла в XML формате
    config = ParamHandler.get_instance('./params.pickle')
    config.read() # читаем данные из текстового файла
    print(config.params)
