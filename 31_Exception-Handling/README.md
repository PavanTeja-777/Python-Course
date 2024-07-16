# Exception Handling
- Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. 
- Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

# Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# Python try...except
try-except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed. 

## Syntax:
```python
try:
    #statements which could generate exception / error
    ...
except:
    #Soloution of generated exception
    ...
```
## Example:
```python
try:
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

    print(f'The result of num1/num2: {num1/num2}')

except ValueError: # We can specify the exception than can occur
    print("Number entered is not an integer.")

except Exception as e: #To handle any type of Excpetion

    # Exception is a long name, so we can give a alias to it by using 'as'
    print(f'{e} exception has occured')
```

## Output:
case1:
```
Enter an integer: 6.022
Number entered is not an integer.
```
case2:
```
Enter an integer: 10
Enter another integer: 0
division by zero exception has occured
```
case3:
```
Enter an integer: 10
Enter another integer: 2
The result of num1/num2: 5.0
```