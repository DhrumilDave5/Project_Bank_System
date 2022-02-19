money = []
data = []
aadhaar = []
name_pass = []
file = open('customer.txt', 'r')
for i in file:
    user = eval(i[:-1])
    money_ = user[3]
    aadhaar_ = user[5]
    ele = [user[1].lower(), user[2].lower()]
    data.append(user)
    money.append(money_)
    aadhaar.append(aadhaar_)
    name_pass.append(ele)
file.close()
