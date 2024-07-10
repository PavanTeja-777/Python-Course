# Tuples

- Tuples are same as Lists. 
- Tuple items are separated by commas and enclosed within round brackets ().
- Tuples are unchangeable meaning we can not alter them after creation. (Immutable)

Example :
```py
eg = ('Python', 7, True, None)
print(eg)
```
Output:
```
('Python', 7, True, None)
```

## Indexing & Slicing:

- Tuple indexing & Slicing is same as of List.

## How to Modify Tuples

As we already know Tuples are immutable, for modifying a Tuple we need to convert it into List then modify and turn it back into Tuple like.

```py
lang = ('Js','Java','C#')

lang = list(lang)ca
lang.insert(0,'Python')
lang = tuple(lang)

print(lang)
```

Output:
```
('Python', 'Js', 'Java', 'C#')
```

# Tuple methods
As Tuple is immutable type of collection of elements it have limited built in methods.They are explained below

## count()
The count() method of Tuple returns the number of times the given element appears in the Tuple.

### Example
```python
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(f'Count of 3 in Tuple1 is: {Tuple.count(3)}')
```
### Output
```
3
```

# index() 
The index() method returns the first occurrence of the given element from the Tuple.

### Example
```python
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(f'First occurrence of 3 is at index: {Tuple.index(3)}')
```
#### Output
```
3
```
Note: This method raises a ValueError if the element is not found in the Tuple.