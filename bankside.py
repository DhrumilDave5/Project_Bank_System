import account
import display
import interest

print("=" * 75 + "\nWELCOME TO KENDRIYA NATIONAL BANK\n" + "=" * 75 + "\n")

while True:
    print("Given below are the actions that you can perform:\n"
          "1) Create new account\n"
          "2) Delete an account\n"
          "3) Display details of all customers\n"
          "4) Display total money in bank\n"
          "5) Calculate simple interest\n"
          "6) Calculate compound interest\n"
          "7) Quit\n")
    choice = input("Enter your choice (from 1-7): ")
    print("\n" + "=" * 75 + "\n")
    if choice == "1":
        account.open_account()
    elif choice == "2":
        account.delete_account()
    elif choice == "3":
        display.customers()
    elif choice == "4":
        display.total_money()
    elif choice == "5":
        interest.simple()
    elif choice == "6":
        interest.compound()
    elif choice == "7":
        print("Thank You for choosing Kendriya National Bank!\n")
        break
    else:
        print("Invalid choice!")
    print("\n" + "=" * 75 + "\n")
