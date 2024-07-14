# eg
prg_lang = {
    'Python': 1991,
    'Java': 1995,
    'C++': 1983,
    'JavaScript': 1995,
    'Ruby': 1995
}
print('Dictionary:', prg_lang)

# Accessing a value using a key
year_python = prg_lang['Python']
print('\nPython was invented in:', year_python)

# Adding a new key-value pair to the dictionary
prg_lang['Swift'] = 2014
print('\nUpdated Dictionary:', prg_lang)

# Removing a key-value pair from the dictionary
del prg_lang['Java']
print('\nDictionary After Removing Java:', prg_lang)

# Iterating over dictionary
print('\nIterating Over the Dictionary:')
for language, year in prg_lang.items():
    print(f'{language} was invented in {year}')

# Dictionary Methods

# keys()
keys = prg_lang.keys()
print('\nKeys:', keys)

# values()
values = prg_lang.values()
print('Values:', values)

# items()
items = prg_lang.items()
print('Items:', items)

# get()
year = prg_lang.get('Python')
print('Get method (Python):', year)

# pop()
prg_lang.pop('C++')
print('After pop (C++):', prg_lang)
