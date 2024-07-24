# Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined class are created using the `class` keyword.

## Creating a Class:
Let us now create a class using the class keyword.
 
```py
class Language:
    name = 'Python'
    invented = 1989

    def print_details(self):
        print(f'{self.name} was invented in {self.invented}')
```

## Creating an Object:
Object is the instance of the class used to access the properties of the class
Now lets create an object of the class.

### Example:
```py
py = Language()
java = Language()
```

## Accessing Objects properties
The properties of an object can be accessed through `.` operator.
```py
java.name = 'Java'
java.invented = 1995

py.print_details()
java.print_details()
```
### Example:
```py
class Language:
    name = 'Python'
    invented = 1989

    def print_details(self):
        print(f'{self.name} was invented in {self.invented}')

py = Language()
py.print_details()
```

### Output:
```
Python was invented in 1989
Java was invented in 1995
```

# Note
- we use `self` keyowrd in class methods to refer to the same instance