balance = 5000
pin = "4321"

while True:

   
    print("1. Balance Enquiry")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    user_pin = input("Enter PIN: ")

    if user_pin != pin:
        print("Incorrect PIN!")
        continue

    option = input("Select Option: ")

    if option == "1":
        print("Available Balance =", balance)

    elif option == "2":
        deposit = float(input("Enter Amount to Deposit: "))
        balance = balance + deposit
        print("Deposit Successful")

    elif option == "3":
        withdraw = float(input("Enter Amount to Withdraw: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Transaction Successful")
            print("Remaining Balance =", balance)
        else:
            print("Not Enough Balance")

    elif option == "4":
        print("Thank You! Visit Again.")
        break

    else:
        print("Please Enter a Valid Option")