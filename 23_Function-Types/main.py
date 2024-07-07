# Ignore this
stack = [0,'Hello',True]
top = 3

# No Argument, No Return
def wish():
    print('Happy birthday to you')
    print('Happy birthday to you')
    print('Happy birthday to you')

# Varying Argument, No Return
def greet(name):
    print(f'Hello, {name}')

# Varying Argument, Return
def sum(a, b):
    return a+b

# No Argument, Return
def pop():
    top -= 1
    return stack[top]

# Default Argument
def increment(number, increment_by = 1):
    return number + increment_by

n = increment(10)
m = increment(10, 5)
print(n)
print(m)

# Keyowrd Parameter
o = increment(increment_by=9, number=21)
print(o)

# Varying Arguments
def printNames(*names):
    for name in names:
        print(name)

printNames('Python', 'JavaScricpt', 'Go')

# Keyword Arguments
def favLang(**languages):
    for person, language in languages.items():
        print(f"{person}'s favorite language is {language}")

favLang(A="Python", B="JavaScript", C="C++", D="Java")
