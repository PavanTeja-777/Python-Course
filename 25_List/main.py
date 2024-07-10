# List
eg = ['Python', 7, True, None]
print(eg)

# in 
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Green']
if 'Yellow' in colors:
    print('Yellow is present.')
else:
    print('Yellow is absent.')

# List Comprehension 1
languages = ['Python', 'Java', 'Ruby', 'JavaScript', 'C++']

With_O = [item for item in languages if 'o' in item]
print(With_O)

# List Comprehension 2
languages = ['Python', 'Java', 'Ruby', 'JavaScript', 'C++']
moreThan4Letters = [item for item in languages if (len(item) > 4)]
print(moreThan4Letters)

# -------------------------------------------------------------------
# List methods

#sort()
colors = ['voilet', 'indigo', 'blue', 'green']
colors.sort() # Ascending order
print(colors) # sorts based on ASCII Valie

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True) # Descending order
print(num)

#reverse()
colors = ['voilet', 'indigo', 'blue', 'green']
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

#index()
colors = ['voilet', 'green', 'indigo', 'blue', 'green']
print(colors.index('green'))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

#count()
colors = ['voilet', 'green', 'indigo', 'blue', 'green']
print(colors.count('green'))

#copy()
colors = ['voilet', 'green', 'indigo', 'blue']
newlist = colors.copy()
print(colors)
print(newlist)

#append()
colors = ['voilet', 'indigo', 'blue']
colors.append('green')
print(colors)

#insert()
colors = ['voilet', 'indigo', 'blue']

colors.insert(1, 'green')
print(colors)

#extend()
colors = ['voilet', 'indigo', 'blue']
rainbow = ['green', 'yellow', 'orange', 'red']
colors.extend(rainbow)
print(colors)

#Concatenating
colors = ['voilet', 'indigo', 'blue', 'green']
colors2 = ['yellow', 'orange', 'red']
print(colors + colors2)