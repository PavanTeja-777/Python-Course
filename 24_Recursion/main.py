def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def print_triangle(n, i=1):
    if i > n:
        return
    else:
        print('* ' * i)
        print_triangle(n, i + 1)

print_triangle(5)