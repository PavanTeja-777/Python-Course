# Constructors

- A constructor is a special method in a class used to create and initialize an object of a class.
- Constructor is invoked automatically when an object of a class is created.
- A constructor is a unique function that gets called automatically when an object is created of a class.
- The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

## Syntax

```python
def __init__(self):
	# initializations
```

- init is one of the reserved functions in Python, it is known as a constructor.
- \_\_init\_\_ is a **Dunder Method** aka **Magic Method**. We will see more of them in upcoming chapters

## Types of Constructors in Python

1. Default Constructor
2. Parameterized Constructor

## Default Constructor

- When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

### Example:

```py
#class with Default constructor
class Language:
    name = 'Python'
    invented = 1989

    # Default Constructor
    def __init__(self):
        print('This is a default constructor')

    def print_details(self):
        print(f'{self.name} was invented in {self.invented}')

py = Language()
py.print_details()
```

### Output:

```
This is a default constructor.
Python was invented in 1989
```

## Parameterized Constructor

- When the constructor accepts arguments along with self, it is known as parameterized constructor.

- These arguments can be used inside the class to assign the values to the data members.

### Example:

```py
#class with Parameter constructor
class Language:

    # Parameterized Constructor
    def __init__(self,name,invented):
        self.name = name
        self.invented = invented
        print('This is Parameterized Constructor')

    def print_details(self):
        print(f'{self.name} was invented in {self.invented}')

java = Language('Java', 1995)
java.print_details()
```

### Output:

```
This is Parameterized Constructor
Java was invented in 1995
```
