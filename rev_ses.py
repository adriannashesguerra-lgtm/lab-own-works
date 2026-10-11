"""
Prob1: Bank Loan Approval System
    - You are tasked with writing a Python program that determines if an applicant is approved for a bank loan. The program will evaluate the applicant based on four factors:

    - Inputs you need to handle:
            age (integer)
            monthly_income (float or integer)
            credit_score (integer)
            employment_status (string: "Employed", "Self-Employed", or "Unemployed")

    - The Rules (Business Logic):

            Age Check (Top Level):
                If the applicant is younger than 18 or older than 65, automatically return: "Rejected: Age not eligible".
                If the age is valid, proceed to the next checks.

            Employment Check:
                If the employment_status is "Unemployed", return: "Rejected: No active income".
                If "Employed" or "Self-Employed", evaluate their credit score.

            Credit Score & Income Check (The Tricky Part):
                If credit_score is 750 or above:
                    If their monthly_income is 50,000 or more, return: "Approved: Premium Loan".
                    Otherwise, return: "Approved: Standard Loan".

            If credit_score is between 600 and 749 (inclusive):
                This depends on their employment type!
                For "Employed": If income is 30,000 or more, return "Approved: Standard Loan". If less, return "Under Review: Income too low".
                For "Self-Employed": If income is 40,000 or more, return "Approved: Standard Loan". If less, return "Under Review: High Risk".
                
            If credit_score is below 600:
                Return: "Rejected: Low Credit Score".
"""
print("Welcome to the Bank")
age = int(input("Enter your age: "))
mon_in = float(input("How much is your monthly income in pesos? "))
cre_scr = int(input("Enter your credit score: "))
emp_stat = input("Enter your employment status: (Employed, Self-Employed, or Unemployed): ")

if 18 <= age <= 65:
    if emp_stat.strip().title() == "Unemployed":
        print("Rejected: No active income")
    elif emp_stat.strip().title() == "Employed" or emp_stat.strip().title() == "Self-Employed":
        if cre_scr >= 750:
            if mon_in >= 50000:
                print("Approved: Premium Loan")
            else:
                print("Approved: Standard Loan")
        elif 600 <= cre_scr <=759:
            if emp_stat.strip().title() == "Employed":
                if mon_in >= 30000:
                    print("Approved: Standard Loan")
                else:
                    print("Under Review: Income too low")
            elif emp_stat.strip().title() == "Self-Employed":
                if mon_in >= 40000:
                    print("Approved: Standard Loan")
                else: 
                    print("Under Review: High Risk")
        else:
            print("Rejected: Low Credit Score")
else:
    print("Rejected: Age not eligible")
    
# same output pero naka define   
def calcu(age, mon_in, cre_scr, emp_stat):
    if 18 <= age <= 65:
        if emp_stat == "Unemployed":
            return "Rejected: No active income"
        elif emp_stat == "Employed" or emp_stat == "Self-Employed":
            if cre_scr >= 750:
                if mon_in >= 50000:
                    return "Approved: Premium Loan"
                else:
                    return "Approved: Standard Loan"
            elif 600 <= cre_scr <=759:
                if emp_stat == "Employed":
                    if mon_in >= 30000:
                        return "Approved: Standard Loan"
                    else:
                        return "Under Review: Income too low"
                elif emp_stat == "Self-Employed":
                    if mon_in >= 40000:
                        return "Approved: Standard Loan"
                    else:
                        return "Under Review: High Risk"
                else: 
                    return "Under Review: High Risk"
        else:
            return "Rejected: Low Credit Score"
    else:
        return "Rejected: Age not eligible"
    
def main():
    print("Welcome to the Bank")
    age = int(input("Enter your age: "))
    mon_in = float(input("How much is your monthly income in pesos? "))
    cre_scr = int(input("Enter your credit score: "))
    emp_stat = input("Enter your employment status: (Employed, Self-Employed, or Unemployed): ").strip().title()
    print(calcu(age, mon_in, cre_scr, emp_stat))
    
main()

"""
Prob2: The Automated Barista 
    - Right now, if someone types "twenty" instead of "20" for their age in your bank program, 
    the whole program crashes with a ValueError. We fix this with Error Handling. Additionally, when you have a menu of specific choices, 
    match-case (introduced in Python 3.10) is much cleaner than writing a massive wall of if-elif-else statements.

    Your Task: Write a program for a coffee shop kiosk.

    The Prompt: Ask the user to enter the number corresponding to their coffee size:
        1 for Small (₱100)
        2 for Medium (₱130)
        3 for Large (₱160)

    Error Handling (try-except):
        Wrap your input() inside a try block and attempt to convert it to an int.
        If the user types a letter or word (like "Small" or "one"), use an except ValueError: block to print: "Invalid input. Please enter a number."

    Match-Case:
        If the input successfully converts to an integer, pass that integer into a match statement.
        Write a case for 1, 2, and 3 that prints the corresponding size and price (e.g., "You ordered a Medium coffee for ₱130.").
        Write a catch-all case (case _:) for any other number (like 4 or 99) that prints: "Size not found on the menu."
"""
try:
    choice = int(input("Enter the number corresponding to the coffee of your liking: 1 for small, 2 for medium, 3 for large: "))
except ValueError:
    print("Invalid Input, Please enter a number.")

match choice:
    case 1:
        print("You ordered a small coffee for ₱100.")
    case 2:
        print("You ordered a medium coffee for ₱130.")
    case 3:
        print("You ordered a large coffee for ₱160.")
    case _:
        print("Size not found on the menu.")

# same output pero naka define
def size(choice):
    match choice:
        case 1:
            return "You ordered a small coffee for ₱100."
        case 2:
            return "You ordered a medium coffee for ₱130."
        case 3:
            return "You ordered a large coffee for ₱160."
        case _:
            return "Size not found on the menu."
        
def main():
    try:
        choice = int(input("Enter the number corresponding to the coffee of your liking: 1 for small, 2 for medium, 3 for large: "))
    except ValueError:
        print("Invalid Input, Please enter a number.")
        return

    print(size(choice))

main()


"""
Prob3: The Airline Cargo Loader
    - You are writing the software for an airline cargo loader. The system receives a list of baggage weights (in kilograms). 
    You need to loop through this list to calculate the total weight loaded and the extra fees collected.
    Here is your starting code:

        baggages = [12, 25, 35, 18, 40, 15, 22, 10]
        total_weight = 0
        total_fees = 0

   The Rules (Inside the loop):
        - The Overweight Reject: If a bag is strictly greater than 30 kg, it is too heavy for the loaders. 
        Print "Bag of [weight]kg rejected." and immediately skip to the next bag in the list. (Hint: use continue).
        
        - The Fee: If a bag is between 21 and 30 kg (inclusive), it is allowed, but you must add 500 to the total_fees.
        
        - The Cargo Limit (The Tricky Part): The plane's cargo hold has a maximum capacity of 100 kg. 
        Before you add a bag's weight to total_weight, you must check if adding it will exceed 100. 
        If it does, print "Cargo full! Stopping." and halt the entire loading process entirely. (Hint: use break).
        
        - The Accumulator: If the bag is accepted and fits the cargo limit, add its weight to total_weight.
"""

baggages = [12, 25, 35, 18, 40, 15, 22, 10]
total_weight = 0
total_fees = 0


for weight in baggages:
    if weight >30:        
        print(f"Baggage weight {weight}kg rejected")
        continue

    if total_weight + weight > 100:
        print("Cargo full! Stopping")
        break
    
    total_weight += weight
    
    if weight > 20:
        total_fees += 500
        

print(f"Final Weight: {total_weight}\nTotal fee: {total_fees}")

# same output pero naka define
def kuha(baggages, total_weight, total_fees):
    for weight in baggages:
        if weight >30:        
            print (f"Baggage weight {weight}kg rejected")
            continue

        if total_weight + weight > 100:
            print("Cargo full! Stopping")
            break
        
        total_weight += weight
        print(f"Current weight: {total_weight}")
        if weight > 20:
            total_fees += 500
            print(f"Total fee: {total_fees}")
        
    return total_weight, total_fees
def main():
    baggages = [12, 25, 35, 18, 40, 15, 22, 10]
    total_weight = 0
    total_fees = 0
    final_w, final_f = kuha(baggages, total_weight, total_fees)
    
    print("-----")
    print(f"Final Weight: {final_w}\nFinal fee: {final_f}")
    
main()

"""
Prob4: The ATM Cash Dispenser
    - You are programming the withdrawal system for a local ATM. The user starts with a set balance, 
    and they can keep withdrawing money as many times as they want—until they either choose to exit, 
    or their account goes dry. Your Starting Code:

        Python
        balance = 5000

   The Rules:
    - The Loop Condition: Set up your loop to run as long as the user still has money. (Hint: while balance > 0:)
    
    - The Input: Inside the loop, ask the user for the withdrawal amount: 
    "Enter amount to withdraw (or type 0 to exit): " (Make sure to convert it to an integer).
    
    - The Exit (Manual): If the user types 0, print "Transaction cancelled." 
    and stop the loop completely using break.
    
    - Insufficient Funds: If the user tries to withdraw an amount greater than their current balance, 
    print "Error: Insufficient funds. Your balance is ₱[balance].". 
    Do not subtract the money, and use continue to restart the loop so they can try again.
    
    - Successful Withdrawal: If the amount is valid (less than or equal to the balance), 
    subtract it from balance and print "Dispensing ₱[amount]... Remaining balance: ₱[balance]".
    
    - The Exit (Automatic): If the user withdraws exactly their remaining balance, the balance becomes 0. 
    The while balance > 0: condition will naturally become False and the loop will end on its own.
    
    - Final Goodbye: Outside and after the loop, print: "Thank you for banking with us! Final balance: ₱[balance]".
"""

bal = 50000
while bal > 0:
    print (f"Current Balance: {bal}")
    amt = int(input("Enter amount to withdraw: (or type 0 to exit) "))
    if amt == 0:
        print ("Transaction cancelled")
        break
    if amt > bal:
        print ("Error: Insufficient funds")
        continue
    else:
        bal -= amt
        
    print ("Transaction successful. Dispersing:", f"{amt:.2f}", "New balance:", f"{bal:.2f}")
        

print ("Final balance:", f"{bal:.2f}")

# same output pero naka define
def withdraw(bal):
    while bal > 0:
        print (f"Current Balance: {bal}")
        amt = int(input("Enter amount to withdraw: (or type 0 to exit) "))
        if amt == 0:
            print ("Transaction cancelled")
            break
        if amt > bal:
            print ("Error: Insufficient funds")
            continue
        else:
            bal -= amt
            
        print ("Transaction successful. Dispersing:", f"{amt:.2f}", "New balance:", f"{bal:.2f}")
        
def main():
    bal = 50000
    withdraw(bal)
    print ("Final balance:", f"{bal:.2f}")