# Comparison Operators

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

print('---------------------------')

# Logical Operators
condition1 = True
condition2 = False

print(condition1 and condition2) # returns True If both the values are True 
print(condition1 or condition2)  # returns True If atlest one value is True 
print(not condition1)            # # returns True If False and Vise-Versa

print('---------------------------')

# Conditional Statements

#if

havingSkills = True
if havingSkills:
    print('You may get a good package!')

#if-else

havingSkills = False
if havingSkills:
    print('You may get a good package!')

else:
    print('Make projects to get skills!')

#if-elif-else

havingSkills = False
havingMarks = True

if havingSkills:
    print('You may get a good package!')

elif havingMarks:
    print('Having only marks is not enough. Get skills!')

else:
    print('Make projects to get skills! and learn Concepts')
