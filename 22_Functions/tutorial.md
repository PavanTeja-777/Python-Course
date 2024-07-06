# Functions
- A function is a block of code that performs a specific task whenever it's invoked (called). 

- For a neat and good programs, when we have large amounts of code or repeated code, we can take the logic apart and use the function where ever its needed

There are two types of functions:

## 1. Built-in functions
These functions are defined and pre-coded in Python such as :  
`min()`, `max()`, `len()`, `sum()`, `type()`, `range()`, `dict()`, `list()`, `tuple()`, `set()`, `print()`, etc.
 

## 2. User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

### Syntax:
```py
def function_name(parameters):
    pass # Code here
```

### Creating a function

Eg:

```py
print('Hello, User')
print('Hello, Follower')
print('Hello, Reader')
```

Here we have statements like this we can see that the program is greeting users Hello, so we can convert them into a function by taking out the logic 

```py
def greet(name):
    print(f'Hello, {name}')
```

- Creating a function isn't enough we should also call it

### Calling a function:
We will call a function by giving the function name, followed by parameters (if any) in the parenthesis.

For eg:
- We can call the above function `greet` by doing like this

```py
greet('User')
greet('Follower')
greet('Reader')
```

Output:

```
Hello, User
Hello, Follower
Hello, Reader
```