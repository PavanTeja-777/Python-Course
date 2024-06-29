#Nested-If
#Propgram to comapre 2 numbers if they are whole numbers

n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))

if n1 < 0 or n2 < 0:
    print("Please enter whole numbers only")
else:
    if n1 < n2:
        print(f'{n1} is less than {n2}')
    elif n1 > n2:
        print(f'{n1} is greater than {n2}')
    else:
        print(f'{n1} is equal to {n2}')

#Ternary Operator
#Program to find max number

m1 = int(input("Enter First number: "))
m2 = int(input("Enter Second number: "))

print('The maximum number is',m1 if m1> m2 else m2)