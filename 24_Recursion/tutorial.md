# Recursive Functions

- A function can call to another function but calling a function itself is called as Recursion

- It's widely used when we want to implement same logic again and again on same variable

### Examples for Recursion

**Example 1**:
```py
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

Output:
```
120
```

**Example 2**:
```py
def print_triangle(n, i=1):
    if i > n:
        return
    else:
        print('* ' * i)
        print_triangle(n, i + 1)

print_triangle(5)
```

Output:
```
*
* *
* * *
* * * *
* * * * *
```