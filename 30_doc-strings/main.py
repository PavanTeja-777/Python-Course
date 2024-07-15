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
    return a*a

print(square(3.3))
print(square.__doc__) #prints the docstr

#These are not docstr
def square(n):
    a = n
    '''Takes in a number n, returns the square of n'''
    # This is not a docstr, a docstr is written immediaty after a function, module or class
    return a**2

print(square.__doc__) # This prints None