import data


def account_inserter():
    file = open("customer.txt", "a+")
    file.seek(0)
    index = 1 + len(file.readlines())
    print("Fill Out The Following Form To Open Your Account In Kendriya National Bank ")
    name = input("Enter Your Name=")
    password = input("Enter Your Password=")
    money = int(input('Enter the amount of money in your account='))
    aadhaar_ = int(input("Enter Your Aadhaar Number="))
    email = input("Enter Your Email id=")
    if aadhaar_ in data.aadhaar:
        print('Your Aadhaar number is invalid ,it exist in our database with an existing user.')
        print('Account is not added to the system.')
        return
    if [name.lower(), password.lower()] in data.name_pass:
        print('User with your given password and name exist in our database.')
        print('Account is not added to the system.')
        return
    data.aadhaar.append(aadhaar_)
    details = [index, name, password, money, email, aadhaar_]
    file.write(str(details) + "\n")
    file_name = 'history\\' + name.lower() + password.lower() + '.txt'
    new_file = open(file_name, 'w')
    file.flush()
    file.close()
    new_file.close()
    print('Your account is successfully added.')
