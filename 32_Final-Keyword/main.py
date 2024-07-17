#syntax
try:
    #statements which could generate exception / error
    ...
except:
    #Soloution of generated exception
    ...
finally:
    #the code that should be executed at any cost
    ...

#eg
def div():
    try:
        num1 = int(input('Enter an integer: '))
        num2 = int(input('Enter another integer: '))

        return num1/num2

    except ValueError: # We can specify the exception than can occur
        return 'VALUE IS NOT CORRECT OCCURED!!'

    except Exception as e:
        return f'{str(e).capitalize()}, error has occured'
    
    finally:
        print('Thanks for using div()')

print(div())