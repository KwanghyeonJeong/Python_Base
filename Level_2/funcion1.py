#define function
def open_account():
    print("A new account has been created.")

def deposit(balance, money):
    print("The deposit is complete. The balance is {0}.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if (balance > money):
        print("The withdrawal is complete. The balance is {0}.".format(balace-money))
        return balance
    else:
        print("The withdrawal was not completed. The balance is {0}.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance-money-commission


# call function
'''
open_account()
balance = 0
balance = deposit(balance,1000)
balance = withdraw(balance,5000)
commission, balance = withdraw_night(balance, 500)
print("The fee is{0}, and the balance is{1}.".format(commission,balance))
'''
