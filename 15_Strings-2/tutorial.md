# String Slicing & Operations on String

## Slicing :
- This method of specifying the start and end index to specify a part of a string is called slicing.
```py
word = 'Python'

# Basic Slicing
print(word[:5])       # Pytho
print(word[5:])       # n
print(word[2:6])      # thon
print(word[-8:])      # Python

# Slicing with step
print(word[::2])      # Pto
print(word[1::2])     # yhn
print(word[::-1])     # nohtyP
print(word[1:5:2])    # yh

# More advanced slicing
print(word[-1:-5:-1]) # noht
print(word[:5:-1])    # (No Output)
print(word[-1:2:-1])  # noh 
print(word[4:0:-2])   # ot

```

## String methods
Python provides a set of built-in methods that we can use to alter and modify the strings.
```py
string = 'Python was invented by Guido Van Rossum'

print(string.upper())       # PYTHON WAS INVENTED BY GUIDO VAN ROSSUM
print(string.lower())       # python was invented by guido van rossum
print(string.title())       # Python Was Invented By Guido Van Rossum
print(string.swapcase())    # pYTHON WAS INVENTED BY gUIDO vAN rOSSUM
print(string.capitalize())  # Python was invented by guido van rossum

print(string.replace('Guido', 'H')) # Python was invented by H Van Rossum

print(string.split()) # ['Python', 'was', 'invented', 'by', 'Guido', 'Van', 'Rossum']


# makes the len of str to n(Parameter) if less then act then places 
# content in centre with given char default char is ' '
print(string.center(50))      #       Python was invented by Guido Van Rossum     
print(string.center(50, '.')) # ......Python was invented by Guido Van Rossum.....

print(string.count('a'))           #        

print(string.find('was'))          # 7  (Index)
print(string.index('was'))         # 7  (Index)

# (If given substring is not present)
print(string.find('Microsoft'))    # -1 
print(string.index('Microsoft'))   # ValueError: substring not found 

print(string.endswith('Rossum'))   # True
print(string.startswith('Python')) # True
print(string.isalnum())            # False
print(string.isalpha())            # False

string = '    Python was invented by Guido Van Rossum     '
print(string.strip()) # Python was invented by Guido Van Rossum
```
##
### Note: The comments beside the print statements are Outputs
### Note: The all the operation done with string will return a new string, it will not modify the string