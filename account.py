import os
import data


def open_account():

    with open("customers.txt", "a") as file:

        print("Fill the following form to open your account in Kendriya"
              " National Bank\n")
        print("Note that the username and password are not case sensitive")
        print("i.e. capital and small letters are treated as same\n")

        while True:
            username = input("\nEnter your username: ").upper()
            if len(username) <= 20:
                if username.isalnum():
                    break
                else:
                    print("Username should contain only alphabets and"
                          " digits and no spaces or other characters")
            else:
                print("Username should not be of more than 20 characters")

        while True:
            password = input("\nEnter your password: ").upper()
            break_loop = False
            if 5 <= len(password) <= 10:
                if " " not in password:
                    for i in password:
                        if i in "!@#$%^&*?/<>+-=_":
                            break_loop = True
                            break
                    else:
                        print("Password should contain at least 1 special"
                              " character")
                else:
                    print("Password should not have space")
            else:
                print("Password should be of 5-10 characters")
            if break_loop:
                break

        while True:
            money = input("\nEnter the amount of first deposit: ")
            if money.isnumeric():
                money = int(money)
                break
            else:
                print("Please enter integer value")

        while True:
            email = input("\nEnter your email id: ")
            if email.count("@") == 1 and email.count(".") >= 1 \
                    and "." in email[email.find("@"):]:
                break
            else:
                print("Incorrect format for email is entered, example"
                      " email of correct format: abc@xyz.com")

        while True:
            aadhaar = input("\nEnter your Aadhaar number: ")
            if len(aadhaar) == 12:
                if aadhaar.isnumeric():
                    aadhaar = int(aadhaar)
                    break
                else:
                    print("Please enter integer value")
            else:
                print("Aadhaar number is always 12 digit")

        print("\n" + "-" * 75 + "\n")

        aadhaar_list = [i[4] for i in data.main()]
        if aadhaar not in aadhaar_list:
            names_passwords = [(i[0], i[1]) for i in data.main()]
            if (username.lower(), password.lower()) not in names_passwords:
                details = [username, password, money, email, aadhaar]
                file.write(str(details) + "\n")
                new_file = open("history\\" + username.lower()
                                + password.lower() + ".txt", 'w')
                new_file.close()
                print("Your account is successfully added to the system!")
            else:
                print("An account with the same username and password is"
                      " already registered with our bank")
                print("Account is not added to the system!")
        else:
            print("An account with the same Aadhaar number is already"
                  " registered with our bank")
            print("Account is not added to the system!")


def delete_account():

    with open("customers.txt") as file:

        file.seek(0)
        print("Enter username and password of the account to be deleted")
        username = input("Username: ").upper()
        password = input("Password: ").upper()
        lines = file.readlines()
        print("\n" + "-" * 75 + "\n")

        for i in range(len(lines) - 1):
            user = eval(lines[i][:-1])
            if user[0] == username:
                print("An account with the entered username is registered"
                      " with our bank")
                if user[1] == password:
                    print("The entered password is correct")
                    os.remove("history\\" + user[0].lower()
                              + user[1].lower() + ".txt")
                    lines.remove(str(user) + "\n")
                    print("The account with the username", username,
                          "is deleted successfully!")
                else:
                    print("The entered password is incorrect")
                    print("Account is not deleted!")
                break
        else:
            print("No such account with the entered username is"
                  " registered with our bank!")
