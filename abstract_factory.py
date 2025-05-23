"""
Abstract Factory Design Pattern in Python:
    The Abstract Factory is a creational design pattern 
    that provides an interface for creating families of related or dependent objects
    without specifying their concrete classes.
    While the Factory Method pattern creates a single product, 
    the Abstract Factory pattern creates entire families of related products. 
    It's like a factory of factories.
"""

from abc import ABC, abstractmethod

# Abstract Products
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass

# Concrete Products
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2."

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
    
    @abstractmethod
    def create_product_b(self):
        pass

# Concrete Factories
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()

# Client code
def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(product_a.useful_function_a())
    print(product_b.useful_function_b())

# Usage
print("\nClient: Testing client code with the first factory type:")
client_code(ConcreteFactory1())
print("\nClient: Testing the same client code with the second factory type:")
client_code(ConcreteFactory2())



"""
    ┌───────────────────┐       ┌───────────────────┐
    │  Abstract Factory │       │ Abstract Product A │
    └────────┬──────────┘       └────────┬──────────┘
            │                           │
        ┌────┴────┐               ┌──────┴───────┐
        │         │               │              │
    ┌───▼───┐ ┌───▼───┐       ┌───▼───┐      ┌───▼───┐
    │Factory│ │Factory│       │Product│      │Product│
    │   1   │ │   2   │       │  A1   │      │  A2   │
    └───────┘ └───────┘       └───────┘      └───────┘
                                
                            ┌───────────────────┐
                            │ Abstract Product B │
                            └────────┬──────────┘
                                    │
                                ┌────┴────┐
                                │         │
                            ┌───▼───┐ ┌───▼───┐
                            │Product│ │Product│
                            │  B1   │ │  B2   │
                            └───────┘ └───────┘


    Client ──────► AbstractFactory
                        │
                        │ creates
                        ▼
                ┌─────────────┐
                │             │
                ▼             ▼
        AbstractProductA  AbstractProductB
                │             │
                │             │
                ▼             ▼
        ConcreteProductA  ConcreteProductB
"""

# another example


# Abstract product
class Button(ABC):
    @abstractmethod
    def show(self):
        pass

# Abstract product
class CheckBox(ABC):
    @abstractmethod
    def show(self):
        pass

# concrete product
class WindowsButton(Button):
    def show(self):
        return 'show windows button!'

# concrete product
class WindowsCheckBox(CheckBox):
    def show(self):
        return 'show windows checkbox!'

# concrete product
class MacOsButton(Button):
    def show(self):
        return 'show MacOs button!'

# concrete product
class MacOsCheckBox(CheckBox):
    def show(self):
        return 'show MacOs checkbox!'

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_checkbox(self):
        pass

# concrete factory
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckBox()

# concrete factory
class MacOsFactory(GUIFactory):
    def create_button(self):
        return MacOsButton()
    
    def create_checkbox(self):
        return MacOsCheckBox()

def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.show())
    print(checkbox.show())

print("\nClient: Testing client code with Windows factory:")
client_code(WindowsFactory())
print("\nClient: Testing client code with MacOS factory:")
client_code(MacOsFactory())