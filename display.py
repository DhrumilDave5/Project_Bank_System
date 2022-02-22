import data


def total_money():
    total = 0
    for i in data.main():
        total += i[2]
    print("Total money in the bank is: ", total)


def customers():
    for i in data.main():
        print("User name: ", i[0])
        print("Money in the account: ", i[2])
        print("Email: ", i[3])
        print("Aadhaar number: ", i[4])
        print("\n")
