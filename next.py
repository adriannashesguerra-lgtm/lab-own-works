"""
Python practice for def and file handling
"""

def cal_area_rect (len, wid):
    try:
        return len * wid
    except ValueError:
        print("Please enter valid numbers for length and width.")
        return None
    
def main ():
    try:
        len = float(input("Enter an integer for length: "))
        wid = float(input("Enter an integer for width: "))
        fin_a = cal_area_rect(len, wid)
        if fin_a is not None:
            print(f"The area of the rectangle is: {fin_a}")
    except ValueError:
        print("Please enter valid numbers for length and width.")

main()