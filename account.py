from data import Addhar,NP


def Openaccount():
    file=open("customer.txt","a+")
    file.seek(0,0)
    index=1+((len(file.readlines())))
    print("Fill Out The Following Form To Open Your Account In Kendriya National Bank ")
    FName=input("Enter Your Name=")
    Password=input("Enter Your Password=")
    Money=int(input('Enter the amount of money in your account='))
    aadhar=int(input("Enter Your Adhaar Number="))
    Email=input("Enter Your Email id=")
    if aadhar in Addhar:
        print('Your Addhar number is invalid ,it exist in our database with an existing user.')
        print('Account is not added to the system.')
        return
    if [FName,lower(),password.lower()] in NP:
        print('User with your given password and name exist in our database.')
        print('Account is not added to the system.')
        return
    Details=[index,FName,Password,Money,Email,Aadhar]
    Final=str(Details)
    file.write(Final +"\n")
    print('Your account is successfully added.')
    file.flush()
    file.close()


def account_deleter():
    file=open('customer.txt','r+')
    print('Application to delete an account')
    name=input('Enter name of the account User you want to delete=')
    password=input('Enter password for autorization=')
    users=[]
    deleted=''
    for i in file:
        user=eval(i[0:(len(i)-1)])
        users.append(user)
    for i in users:
        if i[1].lower()==name.lower():
            print('account founded succesfully.')
            if i[2].lower()!=password.lower():
                print('Incorrect user password.')
            else:
                deleted=i
                users.remove(i)
                break
    else:
        print('No such account with your given password exist in our database.')
    if deleted:
        print('your password is correct')
        print('Account is deleted succesfully')
        ind=deleted[0]-1
        for i in range(ind,len(users)):
            users[i][0]=users[i][0]-1
    file.close()
    file=open('customer.txt','w')
    for i in users:
        file.write(str(i)+'\n')
    file.flush()
    file.close()
