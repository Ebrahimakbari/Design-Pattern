"""
Facade Design Pattern:
    The Facade pattern is a structural design pattern that provides
    a simplified interface to a complex subsystem. 
    It defines a higher-level interface that makes the subsystem easier
    to use by hiding the complexities of the underlying system.

Key Components:
    Facade - Provides a simple interface to the complex subsystem
    Subsystem Classes - Complex classes that implement subsystem functionality
    Client - Uses the Facade instead of calling subsystem objects directly
"""

#Subsystem
class Cpu:
    def execute(self):
        print('executing...')


#Subsystem
class Memory:
    def load(self):
        print('loading from memory...')


#Subsystem
class Ssd:
    def read(self):
        print('reading from ssd...')

#Facade
class Computer:
    def __init__(self):
        self.cpu = Cpu()
        self.memory = Memory()
        self.ssd = Ssd()
    
    def start(self):
        self.memory.load()
        self.ssd.read()
        self.cpu.execute()

#Client
def client():
    computer = Computer()
    computer.start()


client()