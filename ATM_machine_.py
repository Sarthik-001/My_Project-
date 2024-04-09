print('\t\t\t\tWelcome to My Bank of Maharashtra\n')

# Constants
MAX_PIN_ATTEMPTS = 3
CORRECT_PIN = "1012"
INITIAL_BALANCE = 50000

# Initialize variables
pin_attempts = MAX_PIN_ATTEMPTS
balance = INITIAL_BALANCE

while pin_attempts > 0:
    pin = input('Please enter your 4-digit PIN: ')
    if pin == CORRECT_PIN:
        print('Please enter your PIN:')

        while True:
            print('Please press 1 for checking balance')
            print('Please press 2 to make a withdrawal')
            print('Please press 3 to deposit')
            print('Please press 4 to return card')

            option = input('What would you like to choose: ')

            if option == '1':
                print('Your balance is', balance)
            elif option == '2':
                withdrawal = float(input("How much would you like to withdraw? (Enter amount): "))
                if withdrawal in [10000, 15000, 20000] and withdrawal <= balance:
                    balance -= withdrawal
                    print("Transaction successful. Your updated balance is", balance)
                else:
                    print("Invalid amount or insufficient balance.")
            elif option == '3':
                deposit = float(input("How much would you like to deposit? (Enter amount): "))
                if deposit > 0:
                    balance += deposit
                    print("Deposit successful. Your updated balance is", balance)
                else:
                    print("Invalid amount.")
            elif option == '4':
                print("Please wait while your card is returned.")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Incorrect PIN. Please try again.")
        pin_attempts -= 1
        if pin_attempts == 0:
            print("Maximum attempts reached. Your card is blocked.")
            break
