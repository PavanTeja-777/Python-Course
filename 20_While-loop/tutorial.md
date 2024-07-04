# While Loop

- While loops will iterate the statements only if the given condition is true.
- Be careful while writing while loop sometime it may become infinity loop and may crash the program

## While loop syntax:

```py
while condition:
    ... # Statements to be executed
```

## While loop examples

```py
count = 5
while (count > 0):
    print(count)
    count = count - 1
```

Output:
```
5
4
3
2
1
```

# Do-while loop

- In Python we don't have do-while loops as other programming languages have but we can make a logic of that like:

```py
sum = 0
while True:
    number = int(input("Enter numbers to sum (Enter Zero to exit): "))
    
    if number == 0:
        break
    
    sum += number
    print(f'The number {number} is added')

print(f'The sum is {sum}')
```

Output:
```
Enter numbers to sum (Enter Zero to exit): 1
The number 1 is added

Enter numbers to sum (Enter Zero to exit): 2
The number 2 is added

Enter numbers to sum (Enter Zero to exit): 3
The number 3 is added

Enter numbers to sum (Enter Zero to exit): 4
The number 4 is added

Enter numbers to sum (Enter Zero to exit): 0
The sum is 10
```