import data
import time


def withdraw(data_):
    amount = int(input("Enter the money you want to withdraw="))
    money = data_[2]
    name = "history\\" + data_[0].lower() + data_[1].lower() + ".txt"
    if amount > money:
        print("sorry you don't have that much balance in your account")
        print("your current balance is", money, "rupees")
    else:
        time_ = time.asctime()
        print("you have withdrawn", amount, "rupees from your account on", time_)
        print("your current balance now is", money - amount, "rupees")
        money -= amount
        file = open(name, "a")
        text = "date=" + time_ + "\namount withdrawn=" + str(amount) \
               + "\nbalance left=" + str(money) + "\n\n\n\n"
        file.write(text)
        file.close()
        data_[2] = money
        file = open("customers.txt", "r")
        users = []
        for i in file:
            user = eval(i[:-1])
            users.append(user)
        for i in users:
            if i[0].lower() == data_[0].lower() \
                    and i[1].lower() == data_[1].lower():
                del i[3]
                i.insert(3, money)
        file.close()
        file = open("customers.txt", "w")
        for i in users:
            file.write(str(i) + "\n")
        file.close()


def deposit(data_):
    new = int(input("Enter the amount of money you want to deposit="))
    money = data_[3]
    name = "history\\" + data_[1].lower() + data_[2].lower() + ".txt"
    money += new
    time_ = time.asctime()
    print("your balance is now", money, "at", time_)
    file = open(name, "a")
    text = "date=" + time_ + "\namount deposited=" + str(new) \
           + "\nbalance left=" + str(money) + "\n\n\n\n"
    file.write(text)
    file.close()
    data_[3] = money
    file = open("customers.txt", "r")
    users = []
    for i in file:
        user = eval(i[0:-1])
        users.append(user)
    for i in users:
        if i[1].lower() == data_[1].lower() and i[2].lower() == data_[2].lower():
            del i[3]
            i.insert(3, money)
    file.close()
    file = open("customers.txt", "w")
    for i in users:
        file.write(str(i) + '\n')
    file.close()


def history(data_):
    print("-" * 25, "Transaction history of", data_[0], "-" * 25)
    name = "history\\" + data_[0].lower() + data_[1].lower() + ".txt"
    file = open(name)
    for i in file:
        print(i, end='')


def login():

    customer_data = []
    username, password = "", ""
    while not customer_data:
        print("Enter username and password of your account to login")
        username = input("Username: ").upper()
        password = input("Password: ").upper()
        for i in data.main():
            if i[0] == username:
                print("Entered username is registered with our bank")
                if i[1] == password:
                    customer_data = i
                    print("Entered password is correct")
                    break
                else:
                    print("Entered password is incorrect")
        else:
            print("No such account with the entered username is"
                  " registered with our bank!")

    print("=" * 75 + "\nWELCOME TO KENDRIYA NATIONAL BANK " + username
          + "\n" + "=" * 75 + "\n")

    while True:
        print("Given below are the actions that you can perform:\n"
              "1) Withdraw money\n"
              "2) Deposit money\n"
              "3) View transaction history\n"
              "4) Quit\n")
        choice = input("Enter your choice (from 1-4): ")
        print("\n" + "=" * 75 + "\n")
        if choice == "1":
            withdraw(customer_data)
        elif choice == "2":
            deposit(customer_data)
        elif choice == "3":
            history(customer_data)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
        print("\n" + "=" * 75 + "\n")


login()
