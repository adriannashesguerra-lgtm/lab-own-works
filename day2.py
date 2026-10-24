"""
day 2, we will do conditional statements and operators
"""

# comparison operators
"""
== is 'equals to'
!= is 'not equals to'
> is 'greater than'
< is 'less than'
>= is 'greater than or equals to'
<= is 'less than or equals to'
"""

# logical operators
"""
and is 'and'
or is 'or'
not is 'not'
"""

# if-elif-else statements

score = int(input("What is your score?: "))

if score == 100:
    print("You got a perfect score!")
elif score >= 85:
    print("You did well!")
elif score >= 70:
    print ("You passed!")
else:
    print("You failed!")
    
# using logical operators in if statements

name = input("What is your name?: ").strip().title()

if len(name) >= 5 and len(name) <= 10:
    print("Your name is between 5 and 10 characters long.")
    
elif len(name) < 5 or len(name) > 10:
    print("Your name is not between 5 and 10 characters long.")

else:
    print("Your name is exactly 5 or 10 characters long.")