from authenticate import verify_password
from authenticate import verify_users
from authenticate import verify_balance
from authenticate import update_balance
def main():
    print('CIBC Bank')
    username=input('Enter your username ')
    user=verify_users()
    if username==user:
        password=input('Enter your password ')
        pass1=verify_password()
        if password==pass1:
            print('Welcome to CIBC bank')
            print('Your Total balance is',verify_balance())
            print('Choose from following options')
            print('1 to Deposit')
            print('2 to Withdraw')
            print('3 to check balance')
            print('4 to exit')
            user_details()
        else:
            print('Wrong password')
            exit()
    else:
        print('No such username')
        exit()

def user_details():
    username=verify_users()
    bank_balance=verify_balance()
    user_option=int(input(''))
    if user_option==1:
        deposit=int(input('Enter the balance you want to depoist '))
        bank_balance=bank_balance+deposit
        update_balance(username,bank_balance)
    elif user_option==2:
        count=0
        while count<5:
            withdraw=int(input('Enter the amount you want to withdraw '))
            count+=1
            if withdraw>bank_balance:
                print('Amount not sufficient Please try again')            
            else:
                bank_balance=bank_balance-withdraw
                update_balance(username,bank_balance) 
                break
    elif user_option==3:
        print('Your Total Balance is',bank_balance)
        exit(2)
    else:
        exit()
    print('Your Total Balance is',bank_balance)

if __name__=="__main__":
    main()
