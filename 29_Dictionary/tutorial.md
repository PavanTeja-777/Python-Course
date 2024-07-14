# Dictionary

- Dictionaries are ordered collections of data items.
- They store multiple items in a single variable.
- Dictionary items are stored as key-value pairs, separated by commas and enclosed within curly braces {}.
- Dictionaries are changeable, meaning we can alter them after creation.

Example :
```py
prg_lang = {
    'Python': 1991,
    'Java': 1995,
    'C++': 1983,
    'JavaScript': 1995,
    'Ruby': 1995
}
print(prg_lang)
```
Output:
```
{'Python': 1991, 'Java': 1995, 'C++': 1983, 'JavaScript': 1995, 'Ruby': 1995}
```

## Accessing Values

- Values can be accessed using their corresponding keys.
    
Example:
```py
year_python = prg_lang['Python']
print('Python was invented in:', year_python)
```
Output:
```
Python was invented in: 1991
```

## Adding & Removing Items
- You can add new key-value pairs or remove existing ones.

Example:
```py
prg_lang['Swift'] = 2014 # Adding
print(prg_lang)

del prg_lang['Java'] # Removing
print(prg_lang)
```
Output:
```
{'Python': 1991, 'Java': 1995, 'C++': 1983, 'JavaScript': 1995, 'Ruby': 1995, 'Swift': 2014}
{'Python': 1991, 'C++': 1983, 'JavaScript': 1995, 'Ruby': 1995, 'Swift': 2014}
```

## Iterating Over a Dictionary
- You can iterate over a dictionary to access keys and values.

Example:
```py
for language, year in prg_lang.items():
    print(f'{language} was invented in {year}')
```
Output:
```
Python was invented in 1991
C++ was invented in 1983
JavaScript was invented in 1995
Ruby was invented in 1995
Swift was invented in 2014
```

# Dictionary Methods

## keys()
This method returns a list of all the keys in the dictionary.

Example:
```py
keys = prg_lang.keys()
print(keys)
```
Output:
```
dict_keys(['Python', 'C++', 'JavaScript', 'Ruby', 'Swift'])
```

## values()
This method returns a list of all the values in the dictionary.

Example:
```py
values = prg_lang.values()
print(values)
```
Output:
```
dict_values([1991, 1983, 1995, 1995, 2014])
```

## items()
This method returns a list of all the key-value pairs in the dictionary.

Example:
```py
items = prg_lang.items()
print(items)
```
Output:
```
dict_items([('Python', 1991), ('C++', 1983), ('JavaScript', 1995), ('Ruby', 1995), ('Swift', 2014)])
```

## get()
This method returns the value for a specified key if the key is in the dictionary.

Example:
```py
year = prg_lang.get('Python')
print(year)
```
Output:
```
1991
```

## pop()
This method removes the item with the specified key name.

Example:
```py
prg_lang.pop('C++')
print(prg_lang)
```
Output:
```
{'Python': 1991, 'JavaScript': 1995, 'Ruby': 1995, 'Swift': 2014}
```
