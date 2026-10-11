# # repetition structure
# # while loop# 
# count = 1
# while count <= 14:
#     print (f"count is {count}")
#     # count is 5
#     count += 1
#     # count = 6
    
# password = input ("Enter your password: ")
# while password != "python":
#     print ("Invalid password, please try again")
#     password = input ("re-enter your password: ")
# print ("Access granted")
    
# # range function
# # for loop
# # range (5)
# # 0, 1, 2, 3, 4
# for i in range (5):
#     print (f"this is loop number {i}")

# # range (1, 11, 2)
# # (start, stop, step)
# # 1, 3, 5, 7, 9
# for i in range (1, 11, 2):
#     print ("*"*i)

# # break and continue statement
# range (1, 11)
# for i in range (1, 11):
#     if i % 2 == 0:
#         continue
    
#     print (i)
    
# for i in range (1, 11):
#     if i == 5:
#         break
    
#     print (i)
# print ("end of the program")

# #lets make match case
# day = "Thursday"
# match day:
#     case "Tuesday":
#         print ("Today is Tuesday, indeed")
#     case "Monday":
#         print ("Today is Monday, indeed")
#     case "Saturday":
#         print ("Today is Saturday, indeed")
#     case _:
#         print ("I do not know what day it is")

# # for loop in adding even numbers using the input of the user
# nums = int(input ("Enter a number: "))

# total = 0
# for num in range (1, nums + 1):
#     if num % 2 == 0:
#         print (num)
#         total  += num
#     else:
#         continue
# print (f"The total of even numbers from 1 to {nums} is {total}")

# # for loop in multiplying numbers to 5
# nums = int(input ("Enter a number: "))

# total = 1
# for num in range (1, nums + 1):
#     print (f"5 x {num} = {5 * num}")
#     num += 1
# # countdown using for loop

# nums = int(input ("Enter a number: "))

# for num in range (nums, 0, -1):
#     print (num)
#     if num == 0:
#         break
# print ("Blast off!")

# # while loop countdown
# num = int(input ("Enter a number: "))
# while num > 0:
#     print (num)
#     num -= 1
    
# else:
#     print ("Blast off!")

# # while loop for adding positive numbers
# tot = 0
# while True:
#     num = int(input ("Enter a number: "))
#     if num < 0:
#         print ("Negative number entered, exiting the loop.")
#         break
#     else:
#         tot += num
# print (f"The total is {tot}")

# # while loop for input validation
# while True:
#     num = int(input ("Enter a number between 1 and 10: "))
#     if 1 < num or num > 10:
#         print ("Invalid input, please try again.")
#     else:
#         print (f"You entered {num}, thank you!")
#         break

# # for loop for continue
# for num in range (1, 20 + 1):
#     if num == 15:
#         break

#     if num % 3 == 0:
#         continue

#     else:
#         print (num)
#         num += 1
   
# # match case for days of the week
# day = input ("Enter a day of the week: [1-7] ")  

# match day:
#     case "1" | "2" | "3" | "4" | "5":
#         print ("It's a weekday.")
        
#     case "6" | "7":
#         print ("It's a weekend.")
    
#     case _:
#         print ("Invalid input, please enter a number between 1 and 7.")

# # nested decision structure
# grade = int(input ("Enter your grade: [1-100] "))
# absent = int(input ("Enter the number of days you were absent: "))
# if 70 <= grade <= 100:
#     if absent <= 3:
#         print ("You passed the course.")
#     else:
#         print ("You failed the course due to excessive absences.")

# else:
#     print ("You failed the course due to low grades.")
    
# # grade calculator using sentinel value
# total = 0
# count = 0
# subs = float(input("how many subjects did you take? [-1 to exit] "))
# while subs != -1:
#     total += subs
#     count += 1
#     subs = float(input("enter your grade [-1 to exit]: "))
# average = total / count
# print (f"Your average is {average:.2f}")

# # Function 1: The Battery Inspector (Nested Decisions)
# def check_power(voltage):
#     print("Checking power module...")
#     if voltage >= 3.0:
#         print(" -> Power is good!")
#         return True  # Sends a "Yes" back to whoever pushed the button
#     else:
#         print(" -> Warning: Power too low!")
#         return False # Sends a "No" back

# # Function 2: The Hardware Tester (For Loop + Break/Continue)
# def test_hardware(parts_list):
#     print("Testing hardware modules...")
#     for part in parts_list:
#         if part == "LED":
#             continue  # Skip LED, we already know it works
            
#         if part == "Burnt_Wire":
#             print(" -> DANGER! Short circuit detected! Stopping test.")
#             break     # Smash the emergency stop!
            
#         print(" -> " + part + " is working perfectly.")

# # Function 3: The MASTER CONTROLLER (While Loop + Calls other functions)
# def boot_up_robot(voltage_level, parts):
#     print("=== INITIATING STARTUP SEQUENCE ===")
    
#     # The Master Controller presses Function 1's button
#     is_safe_to_start = check_power(voltage_level)
    
#     # Nested decision using the answer from Function 1
#     if is_safe_to_start == True:
#         # The Master Controller presses Function 2's button
#         test_hardware(parts)
        
#         # A quick while loop countdown
#         countdown = 3
#         while countdown > 0:
#             print("System starting in...", countdown)
#             countdown = countdown - 1
            
#         print("=== ROBOT IS ALIVE! ===")
        
#     else:
#         pass # TODO: Add an emergency alarm sound later
#         print("=== STARTUP FAILED. Fix the battery. ===")

# # --- NOW WE PLAY WITH THE CODE ---
# my_modules = ["Sensor", "LED", "Motor", "Camera"]

# # Let's try to turn it on with a good battery!
# boot_up_robot(4.2, my_modules)

# print("\n--------------------------\n")

# # Let's try to turn it on with a dead battery!
# boot_up_robot(2.5, my_modules)
    
# # using def for calculator
# def solving (num1, num2, operation):
#     if operation == "addition":
#         return num1 + num2
#     elif operation == "subtraction":
#         return num1 - num2
#     elif operation == "multiplication":
#         return num1 * num2
#     elif operation == "division":
#         if num2 == 0:
#             raise ValueError("Cannot divide by zero.")
#         return num1 / num2
#     elif operation == "modulus":
#         return num1 % num2
#     elif operation == "exponentiation":
#         return num1 ** num2
#     elif operation == "floor division":
#         if num2 == 0:
#             raise ValueError("Cannot perform floor division by zero.")
#         return num1 // num2
#     else:
#         raise ValueError("Invalid operation. Please choose a valid operation.")
    
# def main ():
#     print ("---Welcome to your typical calculator---")
    
#     while True:
#         print ("""
#                 addition
#                 subtraction
#                 multiplication
#                 division
#                 modulus
#                 exponentiation
#                 floor division
#                 exit
#         """)
#         operation = input ("Enter the operation you want to perform [refer to the list above]: ").strip().lower()
#         if operation == "exit":
#             print ("Exiting the calculator.")
#             break
#         try:
#             num1 = float(input ("Enter your first number: "))
#             num2 = float(input ("Enter your second number: "))
#             result = solving(num1, num2, operation)
#             print ("------Calculation Result---")
#             print (f"First Number: {num1}\nSecond Number: {num2}\nOperator used: {operation}")
#             print (f"The result of {num1} {operation} {num2} is: {result}")
#         except ValueError as e:
#             print(e)
                
            
#         except Exception as e:
#             print(f"An error occurred: {e}")

#         print ("Do you want to perform another calculation? (yes/no)")
#         continue_calculation = input().strip().lower()
#         if continue_calculation != "yes":
#             print ("Thank you for using the calculator. Goodbye!")
#             break
        
#     print ("---End of the calculator program---")
# main ()

# # mid term review from the review session
# """
# Control Structure - organizing program to determine the order on which statements are executed

# Sequence Structure - statements are executed one after another in the order they appear, from top to bottom

# Condition Structure - allows the program to make decisions based on certain conditions, using if, elif, and else statements
#                    ex: if, if-else, if-elif-else, nested decisions, match-case

# Comparing strings - using comparison operators to compare strings, such as == (equal), != (not equal), < (less than), > (greater than), <= (less than or equal), >= (greater than or equal)

# ASCII values - A-Z (65-90), a-z (97-122), 0-9 (48-57)

# Nested Decision Structure - a decision structure placed inside another decision structure. 
#                             which is useful when a program needs to check more than one condition, 
#                             where the second condition only needs to be checked if the first condition is true.
                            
# Match Case - used match and case. it can be used when a program needs to compare a value against several possible cases. 
#             case _: is used as a default case when none of the other cases match.
            
# Repetition Structure - allows a program to execute same set of statements multiple times, using loops such as while and for loops.
#                         ex: condition controlled loop (while loop), count controlled loop (for loop), sentinel controlled loop, nested loops
                        
#                         - while loop - repeatedly executes a set of elements as long as specified condition is true. it is called a pre-test loop because the condition is checked before the loop body is executed.
#                         - for loop - repeatedly executes a set of elements for a specified number of times. it is called a post-test loop because the loop body is executed first before the condition is checked.
                        
# Sentinels - a special value that is used to terminate a loop. it is used when the number of iterations is not known in advance. it is also called a flag value or a sentinel value.

# Input Validation - the process of checking if the input provided by the user is valid or not. it is used to ensure that the program can handle unexpected or incorrect input gracefully, without crashing or producing incorrect results.

# Nested Loops - a loop inside another loop. it is used when a program needs to perform a set of operations for each iteration of another loop. it is also called an inner loop or a nested loop.
# """

# # while loop example
# x = 2
# total = 0
# while x <= 10:
#     total += x
#     x *= 2
# print (f"The total is {total}")

# # for loop example
# result = ""

# for i in "PYTHON":
#     if i in "AEIOU":
#         result += i.lower()
#     else:
#         result += i
# print (f"The result is {result}")

# # range function example
# """
# - generates a sequence of numbers, which can be used in for loops or other contexts where a sequence of numbers is needed.
# - range (stop) - generates a sequence of numbers from 0 to stop-1
# - range (start, stop) - generates a sequence of numbers from start to stop-1
# - range (start, stop, step) - generates a sequence of numbers from start to stop-1, incrementing by step, which can be positive or negative.
# """
# for i in range (1, 11):
#     print ("*"*i)
    
# # sentinel controlled loop example
# num = int(input ("Enter a number:  [-1 to exit] "))
# total = 0

# while num != -1:
#     total += num
#     num = int(input ("Enter a number:  [-1 to exit] "))
    
#     if num == -1:
#         break
# print (f"The total is {total}")

# # input validation example
# score = int(input ("Enter your score: [0-100] "))
# while  0 > score or score > 100:
#     print ("Invalid input, please try again.")
#     score = int(input ("Enter your score: [0-100] "))   
# print (f"Your score is {score}, thank you!")

# # nested loop example

for i in range (1, 6):
    for j in range (1, 6):
        for k in range (1, 6):
            for l in range (1, 6):
                for m in range (1, 6):
                    for n in range (1, 6):
                        for o in range (1, 6):
                            for p in range (1, 6):
                                for q in range (1, 6):
                                    for r in range (1, 6):
                                        print (f"{i}{j}{k}{l}{m}{n}{o}{p}{q}{r}")
print ("End of the program")

# import time
# import winsound

# seconds = int(input("Enter the number of seconds for the countdown: "))

# print("Countdown starting...")

# time .sleep(seconds)

# print("Time's up!")
# winsound.Beep(1000, 8000)  # Beep sound for 1 second

# """
# Arithmetic Operations:
# Addition (+): Adds two numbers together.
# Subtraction (-): Subtracts one number from another.
# Multiplication (*): Multiplies two numbers.
# Division (/): Divides one number by another.
# Comparison Operations:
# Floor Division (//): Divides one number by another and returns the largest integer less than or equal to the result.
# Modulus (%): Returns the remainder of a division operation.
# Power (**): Raises a number to the power of another number.
# """
# # using addition
# num1 = 10
# num2 = 5

# print (num1 + num2) 

# # using subtraction
# num1 = 15
# num2 = 5

# print (num1 - num2)

# # using for loop to determine every odd numbers from 1-100
# num = int(input ("Enter a number: "))
# for i in range (1, num + 1):
#     if i %2 == 0:
#         continue
#     else:
#         print (i)
# else:
    # print ("End of the program")
    
    
# for i in range (11, 0, -1):
#     print (i)
