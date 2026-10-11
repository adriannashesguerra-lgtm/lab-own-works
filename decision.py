def decision_structure ():
    print ("Welcoe to the Asian Corporation Comissiion")
    product = ['VC', 'WP', 'FP', 'WT']
    product = input("Enter the product that you have sold ['VC', 'WP', 'FP', 'WT']:").upper()
    amount = int(input("Enter the amount of the product sold: "))
    
    com1 = 0.12
    com2 = 0.10
    com3 = 0.15
    if product in ['VC', 'WP']:
        com = amount * com1
    elif product in 'FP':
        com = min(amount * com2, 400)
    elif product in 'WT':
        com = max(amount * com3, 950)
    else:
        print ("You have entered an invalid input")
        return
   
    print ("\n======Summary======")
    print (f"product: {product}")
    print (f"price: {amount:.2f}")
    print (f"comission: {com:.2f}")
decision_structure()