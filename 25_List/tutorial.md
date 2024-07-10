# List

- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

Example :
```py
eg = ['Python', 7, True, None]
print(eg)
```
Output:
```
['Python', 7, True, None]
```

## Indexing & Slicing:

- List indexing & Slicing is same as of Strings.

## in
We can check if a given item is present in the list. This is done using the `in` keyword.
```py
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Green']
if 'Yellow' in colors:
    print('Yellow is present.')
else:
    print('Yellow is absent.')
```
#### Output:

```
Yellow is present.
```
- If the value is not present it returns False.

## List Comprehension
List comprehensions are used for creating new lists from other iterables.

### Syntax:
```py
List = [Expression(item) for item in iterable if Condition]
```

**Expression**: It is the item which is being iterated.

**Iterable**: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

**Condition**: Condition checks if the item should be added to the new list or not. 

 

### Example 1: Accepts items with the small letter “o” in the new list 
```py
languages = ['Python', 'Java', 'Ruby', 'JavaScript', 'C++']

With_O = [item for item in languages if 'o' in item]
print(With_O)
```
### Output:
```
['Python']
```

### Example 2: Accepts items which have more than 4 letters
```py
languages = ['Python', 'Java', 'Ruby', 'JavaScript', 'C++']

MoreThan4Letters = [item for item in languages if (len(item) > 4)]
print(MoreThan4Letters)
```
### Output:
```
['Python', 'JavaScript']
```

# List Methods

## sort()
This method sorts the list in ascending order. The original list is updated

### Example 1:
```py
colors = ['violet', 'indigo', 'blue', 'green']
colors.sort() # Ascending order
print(colors) # sorts based on ASCII Valie

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True) # Descending order
print(num)
```
### Output:
```
['blue', 'green', 'indigo', 'violet']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
``` 

## reverse()
This method reverses the order of the list. 

#### Example:
```py
colors = ['violet', 'indigo', 'blue', 'green']
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```
#### Output:
```
['green', 'blue', 'indigo', 'violet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
```

## index()
This method returns the index of the first occurrence of the list item.

#### Example:
```py
colors = ['violet', 'green', 'indigo', 'blue', 'green']
print(colors.index('green'))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```
Output:
```
1
3
```

## count()
Returns the count of the number of items with the given value.
#### Example:
```py
colors = ['violet', 'green', 'indigo', 'blue', 'green']
print(colors.count('green'))
```
#### Output:
```
2
```

## copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list. 

#### Example:
```py
colors = ['violet', 'green', 'indigo', 'blue']
newlist = colors.copy()
print(colors)
print(newlist)
```
#### Output:
```
['violet', 'green', 'indigo', 'blue']
['violet', 'green', 'indigo', 'blue']
```

## append():
This method appends items to the end of the existing list.

#### Example:
```py
colors = ['violet', 'indigo', 'blue']
colors.append('green')
print(colors)
```
#### Output:
```
['violet', 'indigo', 'blue', 'green']
```

## insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

#### Example:
```py
colors = ['violet', 'indigo', 'blue']

colors.insert(1, 'green')
print(colors)
```
#### Output:
```
['violet', 'green', 'indigo', 'blue']
```
## extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#### Example 1:
```py
colors = ['violet', 'indigo', 'blue']
rainbow = ['green', 'yellow', 'orange', 'red']
colors.extend(rainbow)
print(colors)
```
#### Output:
```
['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```
## Concatenating two lists:
You can simply concatenate two lists to join two lists.

#### Example:
```py
colors = ['violet', 'indigo', 'blue', 'green']
colors2 = ['yellow', 'orange', 'red']
print(colors + colors2)
```
#### Output:
```
['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```