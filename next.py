# """
# Python practice for def and file handling
# """

# def cal_area_rect (len, wid):
#     try:
#         return len * wid
#     except ValueError:
#         print("Please enter valid numbers for length and width.")
#         return None
    
# def main ():
#     try:
#         len = float(input("Enter an integer for length: "))
#         wid = float(input("Enter an integer for width: "))
#         fin_a = cal_area_rect(len, wid)
#         if fin_a is not None:
#             print(f"The area of the rectangle is: {fin_a}")
#     except ValueError:
#         print("Please enter valid numbers for length and width.")

# main()

"""
simple banking system
"""

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient funds."
    else:
        return balance - amount

def check_balance(balance):
    return balance

def main():
    balance = 1000.0
    while True:
        print("\nWelcome to the Simple Banking System")
        print("""
            1. Deposit
            2. Withdraw
            3. Check Balance
            4. Exit
              """)
        
        ch = input("Enter your choice (1-4): ")
        
        if ch == '1':
            amt = float(input("Enter amount: "))
            if amt <= 0:
                print("Deposit amount cannot be zero.")
            else:
                new_bal = deposit(balance, amt)
                balance = new_bal
                print (f"New Balance: {balance}")
            
            
        elif ch == '2':
            amt = float(input("Enter amount: "))
            new_bal = withdraw(balance, amt)
            if amt <= 0:
                print("Withdrawal amount cannot be zero.")
            elif isinstance(new_bal, str):
                print(new_bal)
            else:
                balance = new_bal
                print(f"New Balance: {balance}")

        elif ch == '3':
            print(f"Current Balance: {check_balance(balance)}")
            
        elif ch == '4':
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
main()

        
