def main():
    data = []
    with open("customers.txt") as file:
        for i in file:
            user = eval(i[:-1])  # as i[-1] will be newline character
            data.append(user)
    return data
