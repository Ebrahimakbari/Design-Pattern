"""
Prototype Design Pattern in Python:
    The Prototype pattern is a creational design pattern that lets you copy
    existing objects without making your code dependent on their classes.
    Instead of creating new objects from scratch, you clone existing instances.

    ┌─────────────────┐
    │    Prototype    │ ← Abstract interface
    │   (Interface)   │
    └────────┬────────┘
            │
            │ implements
            ▼
    ┌─────────────────┐
    │ ConcretePrototype│
    │                 │
    │ + clone()       │ ← Creates copy of itself
    │ + operation()   │
    └─────────────────┘
"""


import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class ConcretePrototype(Prototype):
    def __init__(self):
        self._objects = {}
    
    def register(self, name, obj):
        self._objects[name] = obj
    
    def unregister(self, name):
        del self._objects[name]
    
    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(self._objects[name])
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj

def client(name, obj, **kwargs):
    concrete_prototype = ConcretePrototype()
    concrete_prototype.register(name, obj)
    cloned_obj = concrete_prototype.clone(name, **kwargs)
    return cloned_obj


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_1 = Person('a', 15)
c_person_1 = client('p', person_1, age=20)

print(person_1 is c_person_1)