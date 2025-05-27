"""
Builder Design Pattern:
    The Builder pattern is a creational design pattern that lets you construct
    complex objects step by step. 
    It's particularly useful when you need to create objects with
    many optional parameters or when the construction process is complex.

Key Components:
    Product - The complex object being built
    Builder - Abstract interface defining construction steps
    ConcreteBuilder - Implements the Builder interface
    Director - Controls the construction process (optional)


    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                           Builder Pattern Structure                          │
    └─────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
    │    Director     │         │   <<abstract>>  │         │    Product      │
    │                 │         │    Builder      │         │                 │
    ├─────────────────┤         ├─────────────────┤         ├─────────────────┤
    │ - builder       │◆────────│ # product       │- - - - -│ - part1         │
    ├─────────────────┤         ├─────────────────┤         │ - part2         
    │ + construct()   │         │ + buildPart1()  │         │ - part3         │
    │ + setBuilder()  │         │ + buildPart2()  │         └─────────────────┘
    │ + getResult()   │         │ + getResult()   │
    └─────────────────┘         └─────────────────┘
                                        △
                                        │
                                        │ inherits
                                ┌─────────────────┐
                                │ ConcreteBuilder │
                                │                 │
                                ├─────────────────┤
                                │ + buildPart1()  │
                                │ + buildPart2()  │
                                │ + getResult()   │
                                └─────────────────┘
"""

from abc import ABC, abstractmethod


#Product
class House:
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
    
    def __str__(self):
        return (f'house with foundation={self.foundation}, walls={self.walls}, roof={self.roof}')


# Abstract Builder
class HouseBuilder(ABC):
    def __init__(self):
        self.house = None
        
    def create_new_house(self):
        self.house = House()
    
    def get_house(self):
        return self.house
    
    @abstractmethod
    def build_foundation(self):
        pass
    
    @abstractmethod
    def build_walls(self):
        pass
    
    @abstractmethod
    def build_roof(self):
        pass


#Concrete Builder 1
class HouseOneBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = 'one'
    
    def build_roof(self):
        self.house.roof = 'stone'
    
    def build_walls(self):
        self.house.walls = '10'


#Concrete Builder 2
class HouseTwoBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = 'two'
    
    def build_roof(self):
        self.house.roof = 'wooden'
    
    def build_walls(self):
        self.house.walls = '20'


# Director
class ConstructionDirector:
    def __init__(self):
        self.house_builder = None
    
    def set_house_builder(self, house_builder):
        self.house_builder = house_builder
    
    def get_house(self):
        return self.house_builder.get_house()
    
    def construct(self):
        self.house_builder.create_new_house()
        self.house_builder.build_foundation()
        self.house_builder.build_walls()
        self.house_builder.build_roof()


def client(house_type):
    director = ConstructionDirector()
    director.set_house_builder(house_type)
    director.construct()
    house = director.get_house()
    print(house)


client(HouseOneBuilder())