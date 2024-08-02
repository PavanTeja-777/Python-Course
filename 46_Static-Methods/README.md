# Static Methods

- Static methods in Python are methods that belong to a class rather than an instance of the class. 
- They are defined using the `@staticmethod` decorator and do not have access to the instance of the class (i.e. self). 
- They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

## Syntax:
```py
class Class:

    @staticmethod
    def func_name(parameters):
        # Code
        ...
```

### Example:
```py
class Math:

    @staticmethod
    def add(a, b):
        return a + b

m1 = Math()
print(m1.add(2, 3)) # Output: 5
print(Math.add(2, 3)) # Output: 5
```
In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.
