def Comission_Calculator():
    # get the product code of the product sold
    print("Enter the product code of the product sold (VC, WP, FP, WT): ")
    pc = input().strip().upper()

    # get the sales amount of the product sold
    sales_amount = float(input("Enter the sales amount of the product sold: "))

    if pc in ("VC", "WP"):
        commission_rate = 0.12
        ca = sales_amount * commission_rate

    elif pc == "FP":
        commission_rate = 0.10
        ca = min(sales_amount * commission_rate, 400)

    elif pc == "WT":
        commission_rate = 0.15
        ca = max(sales_amount * commission_rate, 950)

    else:
        print("Invalid product code entered. Please enter a valid product code (VC, WP, FP, WT).")
        return

    print("\n===============================")
    print("Commission Calculator")
    print("-------------------------------")
    print(f"Product Code: {pc}")
    print(f"Sales Amount: {sales_amount:.2f}")
    print(f"Commission Amount: {ca:.2f}")
    print("===============================")
Comission_Calculator()
