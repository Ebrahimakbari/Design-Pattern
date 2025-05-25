"""
Factory Method Design Pattern in Python:
    The Factory Method pattern suggests defining an interface for creating an object,
    but letting subclasses decide which class to instantiate.

    ┌───────────────┐       ┌───────────────┐
    │   Creator     │       │    Product    │
    │ (Abstract)    │       │  (Interface)  │
    └───────┬───────┘       └───────┬───────┘
            │                       │
            │                       │
    ┌───────┴───────┐       ┌───────┴───────┐
    │ConcreteCreator│       │ConcreteProduct│
    └───────────────┘       └───────────────┘
"""

from abc import ABC, abstractmethod

# Product interface
class Document(ABC):
    @abstractmethod
    def create(self):
        pass

# Concrete Products
class PDFDocument(Document):
    def create(self):
        return "PDF document created"

class HTMLDocument(Document):
    def create(self):
        return "HTML document created"

class WordDocument(Document):
    def create(self):
        return "Word document created"

# Creator
class DocumentCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def operation(self):
        # Call factory method to create a Document object
        document = self.factory_method()
        
        # Use the document
        result = f"DocumentCreator: {document.create()}"
        return result

# Concrete Creators
class PDFDocumentCreator(DocumentCreator):
    def factory_method(self):
        return PDFDocument()

class HTMLDocumentCreator(DocumentCreator):
    def factory_method(self):
        return HTMLDocument()

class WordDocumentCreator(DocumentCreator):
    def factory_method(self):
        return WordDocument()

# Client code
def export_document(creator: DocumentCreator):
    print(f"Exporting document: {creator.operation()}")


export_document(PDFDocumentCreator())
export_document(HTMLDocumentCreator())
export_document(WordDocumentCreator())


"""
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │                                      CLIENT CODE                                             │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ export_document(PDFDocumentCreator())                                                        │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            │ 1. Client creates a concrete creator
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ PDFDocumentCreator instance created                                                          │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            │ 2. Client passes creator to function
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ export_document(creator)                                                                     │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            │ 3. Function calls creator.operation()
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ creator.operation()                                                                          │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            │ 4. operation() is defined in the base DocumentCreator
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ Inside DocumentCreator.operation():                                                          │
    │                                                                                              │
    │ document = self.factory_method()  ◄───┐                                                      │
    │                                       │                                                      │
    │                                       │ 5. Calls factory_method() which is                   │
    │                                       │    implemented by PDFDocumentCreator                 │
    │                                       │                                                      │
    │                                       ▼                                                      │
    │                        ┌───────────────────────────────┐                                     │
    │                        │ PDFDocumentCreator.factory_method():                                │
    │                        │                                                                     │
    │                        │ return PDFDocument()  ◄───┐                                         │
    │                        │                           │                                         │
    │                        │                           │ 6. Creates concrete product             │
    │                        │                           │                                         │
    │                        │                           ▼                                         │
    │                        │            ┌───────────────────────────┐                            │
    │                        │            │ PDFDocument instance created                           │
    │                        │            └───────────────┬───────────┘                            │
    │                        │                            │                                        │
    │                        └────────────────────────────┘                                        │
    │                                       │                                                      │
    │                                       │ 7. PDFDocument instance returned                     │
    │                                       │    to operation() method                             │
    │                                       │                                                      │
    │ result = f"DocumentCreator: {document.create()}"  ◄───┐                                      │
    │                                                       │                                      │
    │                                                       │ 8. Calls create() on the             │
    │                                                       │    PDFDocument instance              │
    │                                                       │                                      │
    │                                                       ▼                                      │
    │                                        ┌───────────────────────────────┐                     │
    │                                        │ PDFDocument.create():                               │
    │                                        │                                                     │
    │                                        │ return "PDF document created"                       │
    │                                        └───────────────┬───────────────┘                     │
    │                                                        │                                     │
    │                                                        │ 9. String returned to               │
    │                                                        │    operation() method               │
    │                                                        │                                     │
    │ return result  ───────────────────────────────────────┘                                     │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            │ 10. Result string returned to export_document()
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ print(f"Exporting document: {creator.operation()}")                                          │
    └───────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                            │
                                            │ 11. Final output displayed
                                            ▼
    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
    │ "Exporting document: DocumentCreator: PDF document created"                                  │
    └─────────────────────────────────────────────────────────────────────────────────────────────┘

"""

# Another Example:


# product interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# concrete product
class Dog(Animal):
    def make_sound(self):
        return 'woof'

# concrete product
class Duck(Animal):
    def make_sound(self):
        return 'swage'


#creator
class AnimalCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def operation(self):
        result = self.factory_method()
        print(result.make_sound())


#concrete creator
class DogCreator(AnimalCreator):
    def factory_method(self):
        return Dog()

#concrete creator
class DuckCreator(AnimalCreator):
    def factory_method(self):
        return Duck()


def create_animal(animal:AnimalCreator):
    return animal.operation()


create_animal(DogCreator())
create_animal(DuckCreator())