# What are Strings?
- In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

## Example
```py
name = 'Follower'
print('Hello, ' + name)
```
### Output
```
Hello, Follower
```

## Multiline Strings
If our string has multiple lines, we can create them like this:

```py
a = """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Similique quia ullam neque sed dolores. 
Provident possimus labore vero odio voluptate"""
print(a)
```
Note: When multiline str is not assigned to a variable then it acts as comment
## F-Strings (Formatted String)
If our string is like a template we can use like this, we can create them like this:

```py
lang = 'Python'
review = 'Easy and Powerful'
statement = f'{lang} is a {review} Language'
print(statement)
```
## Accessing Characters of a String
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.

```py
name = 'Python'
print(name[0])
print(name[1])
```

## Looping through the String
We can loop through strings using a for loop like this:

```py
name = 'Python'
for character in name:
    print(character)
```
Above code prints all the characters in the string name one by one!
