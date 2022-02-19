import os


def account_deleter():
    file = open('customer.txt', 'r+')
    print('Application to delete an account')
    name = input('Enter name of the account User you want to delete=')
    password = input('Enter password for authorization=')
    users = []
    deleted = []
    for i in file:
        user = eval(i[:-1])
        users.append(user)
    for i in users:
        if i[1].lower() == name.lower():
            print('account founded successfully.')
            if i[2].lower() != password.lower():
                print('Incorrect user password.')
                break
            else:
                deleted = i
                name = 'history\\' + i[1].lower() + i[2].lower() + '.txt'
                os.remove(name)
                users.remove(i)
                break
    else:
        print('No such account with your given name exist in our database.')
    if deleted:
        print('your password is correct')
        print('Account is deleted successfully')
        ind = deleted[0] - 1
        for i in range(ind, len(users)):
            users[i][0] = users[i][0] - 1
    file.close()
    file = open('customer.txt', 'w')
    for i in users:
        file.write(str(i) + '\n')
    file.flush()
    file.close()
