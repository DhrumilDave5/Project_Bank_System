import data


def total_money():
    """Shows total money in the bank"""
    total = sum(data.money)
    print('Total money in the bank is', total)
    return


def display():
    """Shows details of all customers of bank"""
    for i in data.data:
        print('User name', i[1])
        print('Money in the account=', i[3])
        print('Email is', i[4])
        print('Aadhaar number is', i[5])
        print('\n' * 4)
    return
