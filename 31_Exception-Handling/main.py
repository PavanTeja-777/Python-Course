#syntax
try:
    #statements which could generate exception / error
    ...
except:
    #Soloution of generated exception
    ...

#eg
try:
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

    print(f'The result of num1/num2: {num1/num2}')

except ValueError: # We can specify the exception than can occur
    print("Number entered is not an integer.")

except Exception as e: #To handle any type of Excpetion

    # Exception is a long name, so we can give a alias to it but using 'as'
    print(f'{e} exception has occured')