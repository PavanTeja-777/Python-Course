#  Sets
eg = {'Python', 7, True, None}
print(eg)

# Accessing Sets Element
eg = {'Python', 7, True, None}
for item in eg:
    print(item)

# issubset()
lang = {'Python','C','C++','Java','JS'}
top_lang = {'Python','JS'}

print(top_lang.issubset(lang))

# issuperset()
lang = {'Python','C','C++','Java','JS'}
top_lang = {'Python','JS'}

print(lang.issuperset(top_lang))

# isdisjoint()
old_lang = {'Fortran', 'Cobol', 'Pascal', 'BASIC', 'Lisp'}
latest_lang = {'Kotlin', 'Swift', 'Rust', 'Go', 'TypeScript'}

print(old_lang.isdisjoint(latest_lang))

#add()
lang = {'Python','C','C++','Java','JS'}
lang.add('Rust')
print(lang)

#remove()
lang = {'Python','C','C++','Java','JS'}
lang.remove('C++')
print(lang)

#pop()
lang = {'Python','C','C++','Java','JS'}
popped = lang.pop()
print(lang, popped)

#del
languages = {'Python','C','C++','Java','JS'}
del languages
print(languages)

#clear()
lang = {'Python','C','C++','Java','JS'}
lang.clear()
print(lang)