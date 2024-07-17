# Finally Clause
- The Finally block in exception handling is always executed, regardless of whether an exception occurred. 
- It's used for tasks like closing files, closing database connections, or providing a final message.
- We know that when we use return in any function the interpeter exist form function,
by using Finally, that block of code will be executed
# Syntax:
```
try:
    #statements which could generate exception / error
    ...
except:
    #Soloution of generated exception
    ...
finally:
    #the code that should be executed at any cost
    ...
```

# Example:
```py
def div():
    try:
        num1 = int(input('Enter an integer: '))
        num2 = int(input('Enter another integer: '))
        return num1/num2

    except ValueError:
        return 'Entered Value is not Integer!!'

    except Exception as e:
        return f'{str(e).capitalize()}, error has occurred'
    
    finally:
        print('Thanks for using div()!')

print(div())
```

## Output:
Case 1:
```
Enter an integer: 10
Enter another integer: 2
Thanks for using div()
5.0
```
case 2:
```
Enter an integer: 10
Enter another integer: 0
Thanks for using div()
Division by zero, error has occurred
```

#### TASK: WRITE THE SAME FUNCTION WITHOUT USING FINALLY