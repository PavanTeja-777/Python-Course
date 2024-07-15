# Docstrings in python
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. 
Here is example:
```py
def square(a):
    ''' #starting of docstr
    Takes in a number n, returns the square of n

    Parameters:
    -----------
    n (int or float): The number.

    Returns:
    --------
    int or float: The square of the number.

    Example:
    --------
    >>> square(5)
    25
    #ending of docstr
    '''
    return a**2

print(square(3.3))
print(square.__doc__) #prints the docstr
```
Output:
```
10.889999999999999
 #starting of docstr
    Takes in a number n, returns the square of n

    Parameters:
    -----------
    n (int or float): The number.

    Returns:
    --------
    int or float: The square of the number.

    Example:
    --------
    >>> square(5)
    25
    #ending of docstr

```
Here is an another example:
```py
def square(n):
    a = n
    '''Takes in a number n, returns the square of n'''
    # This is not a docstr, a docstr is written immediaty after a function, module or class
    return a**2

print(square.__doc__) # This prints None
```
Output :
```
None
```
## Python Comments vs Docstrings

### Python Comments
Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

### Python docstrings
As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.