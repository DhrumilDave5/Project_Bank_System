import accountinser
import accountdel
import display
import interest

print('welcome to kendriya national bank')
while True:
    print('''1.>create new account
2.>delete an account
3.>compound interest
4.>simple interest
5.>display total money in Bank
6.>display all accounts detail
7.>quit''')
    choice = input('Enter your choice=')
    if choice == '1':
        accountinser.account_inserter()
    elif choice == '2':
        accountdel.account_deleter()
    elif choice == '3':
        p = float(input("Principal Amount: "))
        r = float(input("Interest Rate (Per Annum): "))
        t = float(input("Time Period (in years): "))
        interest.compound(p, r, t)
    elif choice == '4':
        p = float(input("Principal Amount: "))
        r = float(input("Interest Rate (Per Annum): "))
        t = float(input("Time Period (in years): "))
        interest.simple(p, r, t)
    elif choice == '5':
        display.total_money()
    elif choice == '6':
        display.display()
    elif choice == '7':
        break
    else:
        print('Invalid choice')
