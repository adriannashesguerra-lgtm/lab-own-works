def fruit_type_calculator (ft, tc, qty):
    ft = ft.strip().lower()
    tc = tc.strip().lower()
    
    if ft == "guava":
        return qty *(5.00 if tc == "L" else 10.00)
    elif ft == "mango":
        return (qty / 12) *(15.00 if tc == "L" else 30.00)
    elif ft == "strawberry":
        return (qty / 6) *(8.00 if tc == "L" else 12.00)
    else:
        print ("You have just entered an invalid fruit type, please try again")
        return 0.0
    
def mts ():
    print ("Welcome to mts!")
    print ("Fruits available [guava, mango, strawberry]")
    total = 0.0
    
    fruits = ['guava', 'mango', 'strawberry']
  
    while True:
        ft = input("What fruit type would you like to purchase? (type done if you are finished) ").strip().lower()
        if ft == "done":
            break
        elif ft not in fruits:
            print ("You have entered an invalid input")
            continue
        
        qty = float(input("Enter how many are you going to purchase: "))
    
        tc = input("Enter the type of fruit [I for inported, L for local]").strip().upper()
        if tc not in ["L", "I"]:
            print ("type code not found")
            continue
        price = fruit_type_calculator(ft, tc, qty)
        total += price
        
        more = input("Would you like to add more? [yes or no] ").strip().lower()
        if more != "yes":
            break
        
    print ("\n===MTS===")
    print (f"Fruit/s: {ft}")
    print (f"Quantity: {qty}")
    print (f"Type of fruit: {tc}")
    print (f"Total: P{total:.2f}")
mts ()
