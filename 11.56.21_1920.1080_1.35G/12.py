#nested loop - one loop inside another loop
#nested loop 1
#program to simulate a bank ATM using nested while loop
print('Welcome to Iron Bank of Bravoos ATM')
restart = ('Y')
chances = 3
balance = 3798739.78

while chances >= 0:
    pin = int(input('Enter your 4 digit Pin: '))
    if pin == (2000):
        print('You entered your pin correctly \n')
        while restart not in ('n','NO','no','N'):
            print('Press 1 for Balance\n')
            print('Press 2 for Withdrawl\n')
            print('Press 3 to Pay\n')
            print('Press 4 to Return Card\n')
            option = int(input('Enter your Choice :'))
            if option == 1:
                print('Your Account balance is',balance,'\n')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much would you like to withdraw ? \n'))
                if withdrawl in [100,200,500,2000]:
                    balance = balance - withdrawl
                    print('Your account balance is : ',balance)
                    restart = input('Would you like yo go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank you')
                        break
                    elif withdrawl != [100,200,500,2000]:
                        print('Invalid Amount, Please Retry\n')
                        restart = ('y')
                    elif withdrawl == 1:
                        withdrawl = float(input('Enter your desired amount: '))
            elif option == 3:
                pay_in = float(input('How much would you like to Pay In? '))
                balance = balance + pay_in
                print('\n Your new balance is now ',balance)
                restart = input('Would you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is returned . \n')
                print('Thank you for using our ATM')
                break
            else:
                print('Please enter a correct number \n')
                restart = ('y')
    elif pin != ('2000'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0 :
            print('\n No more tries')
            break
