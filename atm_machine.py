balance = 1200000
tot_dep = 0
tot_with = 0

print ("Welcome to NAKSHI machine!")

while True:
    print ("What would you like to do?")
    print ("type: 1 for deposit, 2 for withdraw, 3 for check your current balance, and 4 to exit")

    choice = input("Enter yoour choice: ").strip().lower()
    
    if choice == "1":
        amount = int(input("Enter your deppsoted amount: "))
        balance = balance + amount
        tot_dep += amount
        print (f"You deposited {amount:.2f}. Your new balance is {balance:.2f}")
    
    elif choice == "2":
        amount = int(input("Enter your deppsoted amount: "))
        if amount > balance:
            print ("You have insufficient funds")
        else:
            balance = balance - amount
            tot_dep += amount
            print (f"You withdrew {amount:.2f}. Your new balance is {balance:.2f}")
                 
    elif choice == "3":
        print (f"Your current balance is: {balance}")
        
    elif choice == "4":
        print ("Thank you for choosing NAKSHI machine!")
        break
    
    else:
        print ("You have just input an invalid choice, please try again")