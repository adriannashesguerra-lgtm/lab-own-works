def Calculator(pc, sales_amount):
    
    if pc in ("VC", "WP"):
        commission_rate = 0.12
        ca = sales_amount * commission_rate
        return ca
    elif pc == "FP":
        commission_rate = 0.10
        ca = min(sales_amount * commission_rate, 400)
        return ca
    elif pc == "WT":
        commission_rate = 0.15
        ca = max(sales_amount * commission_rate, 950)
        return ca
    else:
        print("Invalid product code entered. Please enter a valid product code (VC, WP, FP, WT).")
        return None
    
    
def main():
    # get the product code of the product sold
    pc = input("Enter the product code of the product sold (VC, WP, FP, WT): ").strip().upper()

    # get the sales amount of the product sold
    sales_amount = float(input("Enter the sales amount of the product sold: "))
    ca = Calculator(pc, sales_amount)

    if ca is not None:
        print("\n===============================")
        print("Commission Calculator")
        print("-------------------------------")
        print(f"Product Code: {pc}")
        print(f"Sales Amount: {sales_amount:.2f}")
        print(f"Commission Amount: {ca:.2f}")
        print("===============================")

main()
