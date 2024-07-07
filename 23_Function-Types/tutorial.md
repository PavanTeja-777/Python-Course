# Functions Types

- In Python we can write functions in different ways. Functions can by classified as

## 1. Based on Arguments and return type

- Argument are the variables acts as placeholders in function bodies

1. No Argument, No Return
1. Varying Argument, No Return
1. Varying Argument, Return
1. No Argument, Return

For examples visit [main.py](/23_Function-Types/main.py) on [GitHub](https://github.com/PavanTeja-777)

## 2. Types of Argument

### Default Argument

- Sometimes we just need some value by default like

```py
def increment(number, increment_by = 1):
    return number + increment_by

n = increment(10)
m = increment(10, 5)
print(n)
print(m)
```

Output:
```
10
15
```

### Keyword Argument

- Sometime we just need to pass the parameter in an different order (or) when we don't know the order of arguments then we can use this

```py
def increment(number, increment_by = 1):
    return number + increment_by

o = increment(increment_by=9, number=21)
print(o)
```

Output:
```
30
```

### Varying Arguments
- Sometimes we dont know the fixed number of arguments then we simply put a asterisk `*` before argument then the passed arguments will be turned into tuple. For eg:

```py
def printNames(*names):
    for name in names:
        print(name)

printNames('Python', 'JavaScricpt', 'Go')
```

Output:
```
Python
JavaScricpt
Go
```

### Keyword Varying Arguments
- Sometimes we want parameter names and the values passed by them then we put double asterisk `**` before the argument then it returns a dict:

```py
def favLang(**languages):
    for person, language in languages.items():
        print(f"{person}'s favorite language is {language}")

favLang(A = "Python", B = "JavaScript", C = "C++", D = "Java")
```

Output:
```
A's favorite language is Python
B's favorite language is JavaScript
C's favorite language is C++
D's favorite language is Java
```