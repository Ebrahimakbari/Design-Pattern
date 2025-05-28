"""
Decorator Design Pattern:
    The Decorator pattern is a structural design pattern that
    allows you to attach new behaviors to objects by placing these objects
    inside special wrapper objects that contain the behaviors. 
    It provides a flexible alternative to subclassing for extending functionality.

Key Components:
    Component - The interface for objects that can have responsibilities added dynamically
    ConcreteComponent - The original object to which additional responsibilities can be attached
    Decorator - Abstract class that implements the Component interface and has a Component reference
    ConcreteDecorator - Adds responsibilities to the component
"""

from abc import ABC, abstractmethod

#Abstract Component
class Page(ABC):
    @abstractmethod
    def show(self):
        pass

#Concrete component
class AuthenticationPage(Page):
    def show(self):
        print('show auth page!!')


#Concrete component
class AnonymousPage(Page):
    def show(self):
        print('show anon page!!')


#Abstract Decorator
class PageDecorator(Page, ABC):
    def __init__(self, component):
        self._component = component
    
    @abstractmethod
    def show(self):
        pass

#Concrete decorator
class AuthenticationDecorator(PageDecorator):
    def show(self):
        component = self._component
        username = input('username : ')
        password = input('password : ')
        if username == 'admin' and password == '123':
            component.show()
        else:
            print('not authenticated!')


def client():
    aut_page = AuthenticationPage()
    auth_decorator = AuthenticationDecorator(aut_page)
    auth_decorator.show()

client()