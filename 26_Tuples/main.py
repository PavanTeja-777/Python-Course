#  Tuple
eg = ('Python', 7, True, None)
print(eg)

# in

Tuple = ('Python','Java')

if 'C++' not in Tuple:
    print('C++ is Absent')

# Modifying Tuple
lang = ('Js','Java','C#')

lang = list(lang)
lang.insert(0,'Python')
lang = tuple(lang)

print(lang)

# count()
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(f'Count of 3 in Tuple1 is: {Tuple.count(3)}')

# index()
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(f'First occurrence of 3 is at index: {Tuple.index(3)}')