# Map, Filter and Reduce
- In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. 
- These functions are known as higher-order functions, as they take other functions as arguments.

## map()
- The `map()` function transforms each element in a sequence and returns a new sequence.

Example of map():

```py
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)

print(list(doubled))
```
Output: 
```
[2, 4, 6, 8, 10]
```

## filter()
- The `filter()` function returns a new sequence containing only elements that satisfy a given condition.

Example of filter():

```py
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))
```
Output: 
```
[2, 4]
```

## reduce()
The `reduce()` function applies a function to a sequence and returns a single value.
- It is a part of the functools module in Python.

Example of reduce():

```py
from functools import reduce
numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)
print(sum)
```
Output: 
```
15
```
The reduce() workes as:
```
[1,2,3,4,5]
[3,3,4,5]
[6,4,5]
[10,5]
[15]
```
It is important to note that the reduce function requires the **functools** module to be imported in order to use it.

## Task
- Write a program for calculating factorial without using loops and recursion.
  