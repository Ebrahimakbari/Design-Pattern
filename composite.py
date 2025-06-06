"""
Composite Design Pattern:
    The Composite pattern is a structural design pattern that lets you
    compose objects into tree structures and then work with these structures as
    if they were individual objects.
    It allows you to treat individual objects and compositions of objects uniformly.

Key Components:
    Component - Common interface for both simple and complex objects
    Leaf - Basic element that doesn't have sub-elements
    Composite - Element that has sub-elements (leaves or other composites)
    Client - Works with elements through the Component interface
"""

from abc import ABC,  abstractmethod

#Abstract Component
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

#leaf
class Leaf(Component):
    def __init__(self, name):
        self.name = name
    
    def operation(self):
        return self.name

#Composite
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, child):
        self.children.append(child)
    
    def remove(self, child):
        self.children.remove(child)
    
    def operation(self):
        results = [self.name]
        for child in self.children:
            results.append(child.operation())
        return '\n'.join(results)

#client
def client():
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")

    composite1 = Composite("Composite 1")
    composite2 = Composite("Composite 2")
    
    composite1.add(leaf1)
    composite2.add(leaf1)
    composite2.add(leaf2)

    c1 = composite1.operation()
    c2 = composite2.operation()
    
    print(c1)
    print(c2)


client()