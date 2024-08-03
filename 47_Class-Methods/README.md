# Class Methods

## What are Class Methods?

- A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class.
- Class methods are defined using the `@classmethod` decorator, followed by a function definition. The first argument of the function is always `cls`, which represents the class itself.

## Usage Class Methods

- Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way.

- You could define a class method that creates the instance and returns it to the caller.

- Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

## Syntax
```py
class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
```

In this example, the "factory_method" is a class method that takes two arguments, "argument1" and "argument2." It creates a new instance of the class "ExampleClass" using the `cls` keyword, and returns the new instance to the caller.

## Example
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age)) #This is like calling init
    
    def print_details(self):
        print(f'The age of {self.name} is {self.age}')

p1 = Person.from_string('Python, 33')
p1.print_details() #Output: The age of Python is 33
```

## Conclusion
- Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class.
- They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level.
- With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.

### Note
---
It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.