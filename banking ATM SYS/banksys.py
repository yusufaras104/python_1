print('Welcome to United King Technology Bank ATM')
restart = ('Y')
chances = 3
balance = 999.12
while chances >= 0 :
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('You entered you pin Correctly')
        print('Please Press 1 For Your Balance')
        print('Please Press 2 To Make a Withdrawl')
        print('Please Press 3 To Pay in')
        print('Please Press 4 To Return Card\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your  Balance')
            print('Please Press 2 To Make a Withdrawl')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')
            option = int(input('What Would you like to choose?: '))
            if option == 1:
                print('Your Balance is $', balance)
                restart=input('Would you like to go back? ')
                if restart in ("n","NO","no","N"):
                    print('Thank you')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? '))
    if withdrawl in [10, 20, 30, 40, 60, 80, 100]:
        balance = balance = withdrawl
        print('\nYour Balance is  now $', balance)
        restart = input('Would You you like to go back? ')
        if restart in ('n', 'NO', 'no', 'N'):
            print('Thank You')
            break
        elif withdrawl != [10, 20, 40, 60, 80, 1001]:
            print('Invalid Amount, Please Re-try\n')
        elif withdrawl == 1:
            withdrawl = float(input('Please Enter Desired amout: '))
        
        elif option == 3:
            Pay_in = float(input('How Much Would You Like To Pay In?'))
            balance = balance + Pay_in
            print('^\n Your balance is now $',balance)
            restart (input('Woud you like to go back? '))
            if restart in('no','n','N','NO'):
                print('Thank You')
                break
            elif option == 4:
                print(' Please with whilst your card is Returned ...\n')
                print(' Thank You')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
        elif pin != ('1234'):
            print('Yanlış Şifre')
            chances = chances - 1
            if chances == 0:
                print('\nNO more tries')
                break
