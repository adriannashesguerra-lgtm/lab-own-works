# write a program that checks users age using if-elif-else statement with nested if statement 
age = int(input("Please enter your age: "))
valid_id = False

if age >= 18:
    if valid_id == True:
        print("You are now eligible to vote")
    else:
        print (*"You still need a valid ID to vote")
elif age < 18 and age >= 0:
    print("You are not eligible to vote yet")
else:
    print("Invalid age entered")
    
