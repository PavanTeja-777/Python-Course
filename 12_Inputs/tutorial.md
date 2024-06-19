# Inputs
- In any programming we need to take dynamic values (Inputs from user) instead of declaring the values in Program itself

- Python supports taking inputs from user by via input() function.
input() always returns string  
For eg:

```py
lang_name = input("Enter your fav prog lang name: ")
print(type(lang_name)) # type() is a function which returns the datatype of variable
print(lang_name + " is a good Programming Language")
```
Output :
```
Enter your fav prog lang name: Python
<class 'str'>
Python is a good Programming Language
```