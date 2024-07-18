## Raising Custom errors 
- The raise keyword raises an error and stops the control flow of the program

- I know you are thinking that, from previous post we have trying to stop Exception from crashing our program, but now we are discussing about raising and exception because (read down for more)

- Sometime we want to stop or crash the program.

Syntax: 
```py
raise Exception('Exception name you want to raise')
```

For eg, if we are desgining a banking application and we want to crash the program if the user is not entering correct credentials.

```py
# Assume this is a Banking Application
bal = 5000
password = '5kMoney'
acc_no = 12321

def withdraw(amt):
    global bal
    bal -= amt
    print('Withdraw Successful!')

def main():
    i_acc_no = int(input('Enter Account No: '))
    i_password = input('Enter password: ')
    i_bal = int(input('Enter Amont to withdraw: '))

    if i_acc_no == acc_no and i_password != password:
        raise Exception('Wrong Passowrd')
    
    withdraw(i_bal)

main()
```
**Output** :
```
Enter Account No: 12321
Enter password: 1450
Enter Amont to withdraw: 2000
Traceback (most recent call last):
  File "p:\Python\Course\Code\33_Custom-errors-and-raise\main.py", line 20, in <module>
    main()
  File "p:\Python\Course\Code\33_Custom-errors-and-raise\main.py", line 16, in main
    raise Exception('Wrong Passowrd')
Exception: Wrong Passowrd
```

### Why we need to raise an Exception?

- A user is not aware of code and can make mistakes so need to handle the exceptions , but if you are making a confidential program we need to stop when there is a mistake

- Assume your making a Banking App and you need to crash the program and stop the process when user enters wrong password, if the program is not crashed there may cause vulnerabilities and some can take advantage.

