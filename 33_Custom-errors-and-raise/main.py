# Syntax:
# raise Exception('Exception name you want to raise')

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