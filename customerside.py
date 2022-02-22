import data
import time

cust_data = []


def withdraw():
    amount = int(input('Enter the money you want to withdraw='))
    money = cust_data[2]
    name = 'history\\' + cust_data[0].lower() + cust_data[1].lower() + '.txt'
    if amount > money:
        print("sorry you don't have that much balance in your account")
        print('your current balance is', money, 'rupees')
        return
    else:
        time_ = time.asctime()
        print('you have withdrawn', amount, 'rupees from your account on', time_)
        print('your current balance now is', money - amount, 'rupees')
        money -= amount
        file = open(name, 'a')
        text = 'date=' + time_ + '\namount withdrawn=' + str(amount) + '\nbalance left=' + str(money) + '\n\n\n\n'
        file.write(text)
        file.flush()
        file.close()
        cust_data[2] = money
        file = open('customers.txt', 'r')
        users = []
        for i in file:
            user = eval(i[:-1])
            users.append(user)
        for i in users:
            if i[0].lower() == cust_data[0].lower() and i[1].lower() == cust_data[1].lower():
                del i[3]
                i.insert(3, money)
        file.close()
        file = open('customers.txt', 'w')
        for i in users:
            file.write(str(i) + '\n')
        file.flush()
        file.close()


def deposit():
    new = int(input('Enter the amount of money you want to deposit='))
    money = cust_data[3]
    name = 'history\\' + cust_data[1].lower() + cust_data[2].lower() + '.txt'
    money += new
    time_ = time.asctime()
    print('your balance is now', money, 'at', time_)
    file = open(name, 'a')
    text = 'date=' + time_ + '\namount deposited=' + str(new) + '\nbalance left=' + str(money) + '\n\n\n\n'
    file.write(text)
    file.flush()
    file.close()
    cust_data[3] = money
    file = open('customers.txt', 'r')
    users = []
    for i in file:
        user = eval(i[0:-1])
        users.append(user)
    for i in users:
        if i[1].lower() == cust_data[1].lower() and i[2].lower() == cust_data[2].lower():
            del i[3]
            i.insert(3, money)
    file.close()
    file = open('customers.txt', 'w')
    for i in users:
        file.write(str(i) + '\n')
    file.flush()
    file.close()


def login():
    print('Application to login into your account.')
    name = input('Enter user name=')
    password = input('enter your user-password=')
    if [name.lower(), password.lower()] in data.name_pass:
        print('your user-id and password are correct')
    else:
        print('Given user-id and password is incorrect')
        return
    global cust_data
    cust_data = []
    for i in data.data:
        if [i[1].lower(), i[2].lower()] == [name.lower(), password.lower()]:
            cust_data = i
    print('Welcome to kendriya national bank', name)
    print('''1.> withdraw
2.> deposit
3.> Transaction history
4.> quit''')
    while True:
        choice = input('Enter the number of the service you want=')
        if choice == '1':
            withdraw()
        elif choice == '2':
            deposit()
        elif choice == '3':
            name = 'history\\' + cust_data[1].lower() + cust_data[2].lower() + '.txt'
            file = open(name)
            print('\n' * 2)
            print('----------transaction history of', cust_data[1],
                  '----------------------------------------------------------------------')
            for i in file:
                print(i, end='')
            print('-' * 100)
            print('\n' * 2)
        elif choice == '4':
            break
        else:
            print('Invalid choice')


login()
