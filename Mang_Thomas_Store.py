def compute_price (ft, tc, qty):
    # identify fruit type and type code, then compute price based on quantity
    ft = ft.strip().lower()
    tc = tc.strip().upper()
    
    if ft == "guava":
        return qty * (4.50 if tc == "L" else 25.00)
    elif ft == "pomelo":
        return (qty / 6) * (75.00 if tc == "L" else 100.00)
    elif ft == "avocado":
        return (qty / 12) * (75.00 if tc == "L" else 250.00)
    elif ft == "papaya": 
        return qty * (23.00 if tc == "L" else 25.00)
    elif ft == "mango":
        return qty * (50.00 if tc == "L" else 60.00)
    else:
        print("Invalid fruit type entered. Please enter a valid fruit type (guava, pomelo, avocado, papaya, mango).")
        return 0.0
    
def Mang_Thomas_Store():
    # get the fruit type, quantity, and type code from the user, then compute the total price
    fruits = ["guava", "pomelo", "avocado", "papaya", "mango"]
    print("Welcome to Mang Thomas Store!")
    print("Available fruit types: guava, pomelo, avocado, papaya, mango")
    total = 0
    
    while True:
        fruits = ["guava", "pomelo", "avocado", "papaya", "mango"]
        ft = input("Enter the fruit type (or 'done' to finish): ").strip().lower()
        if ft == "done":
            break
        elif ft not in fruits:
            print("Invalid fruit type entered. Please enter a valid fruit type (guava, pomelo, avocado, papaya, mango).")
            continue
        
        qty = float(input("Enter the quantity: "))
        
        print("Available types: L (Local), I (Imported)")
        tc = input("Enter the type code (L or I): ").strip().upper()
        if tc not in ["L", "I"]:
            print("Invalid type code entered. Please enter a valid type code (L or I).")
            continue
        price = compute_price(ft, tc, qty)
        total += price
        
        more = input("Do you want to add more fruits? (yes/no): ").strip().lower()
        if more != "yes":
            break
        
        
    # display the total price of the fruits purchased
    print("\n===============================")  
    print("Mang Thomas Store")
    print("-------------------------------")
    print(f"Total price: ${total:.2f}")
    print("===============================")
Mang_Thomas_Store()