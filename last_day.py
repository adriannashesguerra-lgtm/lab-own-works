"""
I will be using def function here 
"""

def user_input():
    """
    This function will take input from the user and return it.
    """
    user_data = input("Please enter some data: ")
    return user_data

def main():
    """
    This is the main function that will call the user_input function and print the returned data.
    """
    data = user_input()
    print(f"You entered: {data}")
    
main()