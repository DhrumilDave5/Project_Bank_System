def extract():
    data = []
    with open("customers.txt") as file:
        for i in file:
            user = eval(i[:-1])
            data.append(user)
    return data
