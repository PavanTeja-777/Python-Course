# Advance Conditional Statements
## Nested if-else

- If we have some part of condition which is repeated then we can go with Nested if else statements.
- In a program which result a comparison of 2 numbers which must be whole numbers then we have to write a program like 

```py
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))

if n1 < 0 or n2 < 0:
    print("Please enter whole numbers only")
elif n1 < n2 and (n1 > 0 and n2 > 0):
    print(f'{n1} is less than {n2}')
elif n1 > n2 and (n1 > 0 and n2 > 0):
    print(f'{n1} is greater than {n2}')
elif n1 == n2 and (n1 > 0 and n2 > 0):
    print(f'{n1} is equal to {n2}')
else:
    print('Something went wrong')
```

we can write the above code as 

```py
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))

if n1 < 0 or n2 < 0:
    print("Please enter whole numbers only")
elif n1 > 0 and n2 > 0:
    if n1 < n2:
        print(f'{n1} is less than {n2}')
    elif n1 > n2:
        print(f'{n1} is greater than {n2}')
    else:
        print(f'{n1} is equal to {n2}')
else:
    print('Something went wrong')
```
### Note: while writing Nested if make sure your giving correct indentation

## Ternary Operator

- There are many one liners(Multiple lines can be wriiten in one) in Python. One of them is Ternary Operator.
The syntax for Ternary Operator is like
```py
value_if_condotion_is_true if condition else value_if_condotion_is_false
```

An eg for this is
```py
m1 = int(input("Enter First number: "))
m2 = int(input("Enter Second number: "))

print('The maximum number is',m1 if m1> m2 else m2)
```
This code can be written in normal way too
```py
m1 = int(input("Enter First number: "))
m2 = int(input("Enter Second number: "))

if m1 > m2:
    print('The maximum number is',m1)
else:
    print('The maximum number is',m2)

```