import random
class MyProject(object):
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def greet(self, name):
        return f"Hello {name}!"
    
    def goodbye(self, name):
        return f"Goodbye {name}!"
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

myproject = MyProject("John")
print(myproject.get_name())
print(myproject.greet("Alice"))
print(myproject.goodbye("Bob"))
print(myproject.add(4, 5))
print(myproject.subtract(7, 3))
print(myproject.multiply(5, 2))
try:
    print(myproject.divide(10, 0))
except ValueError as e:
    print(e)