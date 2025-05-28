"""
Singleton Pattern:
    The Singleton pattern ensures a class has only one instance 
    and provides a global point of access to it.
    This is useful when exactly one object is needed to coordinate actions across the system.
"""

# Basic Implementation
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)


# MetaClass Implementation
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        pass


s_1 = MyClass()
s_2 = MyClass()
print(s_1 is s_2)



"""
    obj = MyClass(arg1, arg2)
        │
        ▼
    ┌─────────────────────────────────────┐
    │ type.__call__(MyClass, arg1, arg2)  │ ← Metaclass's __call__ method is invoked
    └─────────────────┬───────────────────┘
                    │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
    ┌──────────────────────┐  ┌────────────────────────────┐
    │ 1. ALLOCATION PHASE  │  │      2. INITIALIZATION     │
    └──────────┬───────────┘  └────────────┬───────────────┘
            │                           │
            ▼                           ▼
    ┌──────────────────────┐  ┌────────────────────────────┐
    │ MyClass.__new__(     │  │ instance.__init__(         │
    │   MyClass,           │  │   arg1,                    │
    │   arg1, arg2         │  │   arg2                     │
    │ )                    │  │ )                          │
    └──────────┬───────────┘  └────────────┬───────────────┘
            │                           │
            ▼                           ▼
    ┌──────────────────────┐  ┌────────────────────────────┐
    │ • Allocates memory   │  │ • Sets up instance         │
    │ • Creates raw object │  │   attributes               │
    │ • Returns instance   │  │ • Performs initialization  │
    └──────────┬───────────┘  └────────────┬───────────────┘
            │                           │
            └─────────────┬─────────────┘
                            │
                            ▼
                    ┌──────────────────┐
                    │ Return instance  │ ← Fully initialized instance is returned
                    └────────┬─────────┘
"""

"""
    When you write code like obj = MyClass(arg1, arg2), here's what happens:

    Python sees you're "calling" a class and invokes its metaclass's __call__ method
    The default implementation in type.__call__ does:
        Call __new__ to create the instance
        Call __init__ to initialize the instance
        Return the instance

    MyClass(arg1, arg2)
        │
        ▼
    type.__call__(MyClass, arg1, arg2)
        │
        ├─▶ instance = MyClass.__new__(MyClass, arg1, arg2)
        │
        ├─▶ instance.__init__(arg1, arg2)
        │
        ▼
    return instance
"""