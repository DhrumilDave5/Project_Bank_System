Money=[]
Data=[]
Addhar=[]
NP=[]
file=open('customer.txt','r')
for i in file:
    user=eval(i[0:(len(i)-1)])
    money=user[3]
    addhar=user[5]
    ele=[user[1].lower(),user[2].lower()]
    Data.append(user)
    Money.append(money)
    Addhar.append(addhar)
    NP.append(ele)
file.close()
