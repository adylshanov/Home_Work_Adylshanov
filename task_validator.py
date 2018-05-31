from abc import ABCMeta, abstractmethod
import re

class Validator(metaclass=ABCMeta):

    def init(self, value):
        self.value = value

    @abstractmethod
    def validate(self, value):
        pass


    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        klass = cls.types.get(name)
        #print(klass)
        if klass is None:
            raise ValidatorException('Validator with name "{}" not found!'.format(name))
        return klass(*args, **kwargs)

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')
        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))
        cls.types[name] = klass

class ValidatorException(Exception):
    def init(self, ext):
        pass

def add_func(type):
    def decorator(cls):
        Validator.add_type(type, cls)
        return cls
    return decorator

@add_func('email')
class EMailValidator(Validator):

    def validate(self, value):
        pattern = '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
        matches = re.search(pattern, value)
        #print(matches)
        #print(value)
        if matches:
            return True
        else:
            return False

@add_func('datetime')
class DateTimeValidator(Validator):
    def validate(self, value):
        pattern = '(\d{,4}[./-]\d{,2}[./-]\d{,4} ?\d?\d?:?\d?\d?:?\d?\d)'
        matches = re.search(pattern, value)
        #print(matches)

        #print(value)
        if matches:
            return True
        else:
            return False


if __name__ == '__main__':
    validator = Validator.get_instance('email')
    print(validator.validate('ya@ya.ru'))

    validator2 = Validator.get_instance('datetime')
    s = '1.9.2017'
    print('Input {}, Output:{}'.format(s, validator2.validate(s)))

    s = '01/02/2017 12:00'
    print('Input {}, Output:{}'.format(s, validator2.validate(s)))
    
    s = '2017-09-01 12:00:00'
    print('Input {}, Output:{}'.format(s, validator2.validate(s)))

