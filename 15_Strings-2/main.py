word = "Python"

# Basic Slicing
print(word[:5])
print(word[5:])
print(word[2:6])
print(word[-8:])

# Slicing with step
print(word[::2])
print(word[1::2])
print(word[::-1])
print(word[1:5:2])

# More advanced slicing
print(word[-1:-5:-1])
print(word[:5:-1])
print(word[-1:2:-1])
print(word[4:0:-2])

string = 'Python was invented by Guido Van Rossum'
str1 = string
print(str1)

print(string.upper())
print(string.lower())
print(string.swapcase())
print(string.capitalize())
print(string.title())

print(string.replace('Guido', 'H'))

print(string.split())

print(string.center(50))
print(string.center(50, '.'))

print(string.count('a'))

print(string.find('was'))
print(string.index('was'))

print(string.find('Microsoft'))
# print(string.index('Microsoft'))

print(string.endswith('Rossum'))
print(string.startswith('Python'))
print(string.isalnum())
print(string.isalpha())

string = '    Python was invented by Guido Van Rossum     '
print(string.strip())