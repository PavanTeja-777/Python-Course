# Basic For loop
n = int(input('Enter a number to print: '))

for i in range(n):
    print(i+1)

# or

for i in range(1,n+1):
    print(i)

# for loop with strings
string = 'Python'

for letter in string: 
    print(letter, end=', ')

print('\n-----------------')

# for loop with list
list_ = [7,'Python',True]

for element in list_:
    print(element)

print('-----------------')

# Nested for loop
languages = ['Python','JavaScricpt','Java']

for language in languages:
    print(language)

    for letter in language:
        print(letter, end=', ')

    print()