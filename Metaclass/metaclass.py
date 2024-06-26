from pprint import pprint 

class Human(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name,bases, class_dict)
        if kwargs:
                for name, value in kwargs.items():
                    setattr(class_, name, value)
        return class_

class Person(object, metaclass=Human, country='INDIA', freedom = True):
    def __init__(self, name, age):
        self.name = name
        self.age = age

pprint(Person.__dict__)

