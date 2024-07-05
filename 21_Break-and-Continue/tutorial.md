# Break and Continue

- We use Break and Countinue in loops to change the order of Iteration

## Break

- Suppose you have written a While loop like ```while(True):``` then it runs forever, to stop the iterations we can use break keyword.

### Example:
```py
counter = 0
while True:
    
    # If we have single statement in a block we can write like this
    if counter == 6: break 

    print(f'Counter value is {counter}')
    counter += 1
```

Output:
```
Counter value is 0
Counter value is 1
Counter value is 2
Counter value is 3
Counter value is 4
Counter value is 5
```

## Continue

- Suppose you want to skip any iteration instead of **Break**ing out of loop then we can use **continue**.

### Example:
```py
for i in range(1,11):

    if i % 2 != 0:
        continue

    print(i)
```

Output:
```
2
4
6
8
10
```