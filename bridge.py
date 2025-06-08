"""
Bridge Design Pattern:
    The Bridge pattern is a structural design pattern that separates an
    abstraction from its implementation so that both can vary independently.
    It's used when you want to avoid permanent binding between an abstraction and its implementation.

Key Components:
    Abstraction - Defines the abstraction's interface and maintains a reference to the Implementor
    RefinedAbstraction - Extends the interface defined by Abstraction
    Implementor - Defines the interface for implementation classes
    ConcreteImplementor - Contains the actual implementation
"""

from abc import ABC, abstractmethod

#Abstraction
class Abstraction(ABC):
    def __init__(self, implementation):
        self._implementation = implementation
    
    @abstractmethod
    def perform_action(self):
        pass

#RefinedAbstraction
class RefinedAbstractionOne(Abstraction):
    def perform_action(self):
        self._implementation.action_implementation()


#RefinedAbstraction
class RefinedAbstractionTwo(Abstraction):
    def perform_action(self):
        self._implementation.action_implementation()

#Implementor
class Implementation(ABC):
    @abstractmethod
    def action_implementation(self):
        pass


#ConcreteImplementor
class ConcreteImplementationOne(Implementation):
    def action_implementation(self):
        print(self.__class__.__name__)


#ConcreteImplementor
class ConcreteImplementationTwo(Implementation):
    def action_implementation(self):
        print(self.__class__.__name__)

#Client
def client():
    c_i_1 = ConcreteImplementationOne()
    c_i_2 = ConcreteImplementationTwo()
    
    r_1 = RefinedAbstractionOne(c_i_1)
    r_2 = RefinedAbstractionOne(c_i_2)

    r_1.perform_action()
    r_2.perform_action()


client()