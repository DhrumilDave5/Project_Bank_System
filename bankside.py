import accountinser
import accountdel
import display
import compound
import simple

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
        compound.compound_interest()
    elif choice == '4':
        simple.simple_interest()
    elif choice == '5':
        display.total_money()
    elif choice == '6':
        display.display()
    elif choice == '7':
        break
    else:
        print('Invalid choice')
