# Introduction to Loops 

- Sometimes we want to execute a group of statements a certain number of times. This can be done using loops. 

Loops are further classified into following main types:

1. For Loop
2. While Loop

## For Loop

- For loops can iterate over a sequence of iterable objects in python.

Iterable objects are:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries - Keys are printed while iterating

## For loop examples

### 1. Strings

```py
string = 'Python'

for letter in string: 
    print(letter, end=', ')
```
Output:
```
P, y, t, h, o, n, 
```

### 2. List

```py
list_ = [7,'Python',True]

for element in list_:
    print(element)
```
Output:
```
7
Python
True
```

### 3. Nested

```py
languages = ['Python','JavaScricpt','Java']

for language in languages:
    print(language)

    for letter in language:
        print(letter, end='-')

    print()
```
Output:
```
Python
P, y, t, h, o, n, 
JavaScricpt
J, a, v, a, S, c, r, i, c, p, t, 
Java
J, a, v, a, 
```

### 4. Range
```py
n = int(input('Enter a number to print: '))

for i in range(n):
    print(i)
```
Output:
```
5
0
1
2
3
4
```
- If only single value passed iteration starts from 0
- We can specify the range by ```range(start,end)``` (Note: end number doesn't iterate)
```py
for i in range(1,11):
    print(i)
```
Output:
```
1
2
3
4
5
6
7
8
9
10
```