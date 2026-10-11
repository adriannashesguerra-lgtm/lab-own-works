# sal = float(input("Enter your salary: "))
# service = int(input("Enter your years of service: "))
# if sal >= 3000:
#     if service >= 2:
#         print("You are qualify for a loan")
#     else: 
#         print("You must have been on your current job for at least 2 years to qualify")
# else:
#     print("You must have a salary of at least $3000 per year to qualify")


# while True:
#     try:
#         sal = float(input("Enter your salary: "))
#         service = int(input("Enter your years of service: "))
   
#         if sal >= 3000:
#             if service >= 2:
#                 print("You are qualified for a loan")
#             else: 
#                 print("You must have been on your current job for at least 2 years to qualify")
#         else:
#             print("You must have a salary of at least $3000 per year to qualify")

#         break  # Exit the loop if inputs are valid
#     except ValueError:
#         print("Invalid input. Please enter numeric values for salary and years of service.")
#     finally:
#         print("Loan qualification check completed.")

# # for loop
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print("*" * num)

# # try, except, else, finally
# try:
#     num1  = float(input("Enter the first integer: "))
#     num2  = float(input("Enter the second integer: "))
#     op = input("Enter the operation (+, -, *, /): ")
#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "/":
#         result = num1 / num2
# except ValueError:
#     print("Invalid input. Please enter numeric values for the integers.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print(f"The result of {num1} {op} {num2} is: {result}")
# finally:
#     print("Operation completed.")
    
# try:
#     total_entries = int(input("Enter the number of entries: "))
# except ValueError:
#     print("Invalid input. Please enter an integer value for the number of entries.")
#     total_entries = 3
    
# for total_entry in range(total_entries):
#     try:
#         score = float(input(f"Enter score {total_entry + 1}: "))
#         if score >= 90 and score <= 100:
#              print("Grade: A")
#         elif score >= 75:
#             print("Grade: B")
#         else:
#             print("Grade: C")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value for the score.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         print(f"Entry {total_entry + 1} completed.")
        
# num = 1

# while num <= 5:
#     print(num)

# program for reviewing if the number is a prime number or not
# while True:
#     try:
#         num = int(input("Enter a number: "))
#         if num > 1:
#             for i in range(2, num):   
#                 if (num % i) == 0:
#                     print(f"{num} is not a prime number")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value for the number.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     else:
#         print(f"{num} is a prime number")
#     try:
#         choice = input("Do you want to check another number? (y/n): ").strip().lower()
#         if choice != "y":
#             print("Program Completed.")
#             break
#         else:
#             continue
#     except ValueError:
#         print("Invalid input. Please enter 'y' or 'n'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def prime(num):
#     if num > 1:
#         for i in range(2, num):   
#             if (num % i) == 0:
#                 return False
#         return True
#     else:
#         return False

# def main():
#     while True:
#         try:
#             num = int(input("Enter a number: "))
#             if prime(num):
#                 print(f"{num} is a prime number")
#             else:
#                 print(f"{num} is not a prime number")
#         except ValueError:
#             print("Invalid input. Please enter a numeric value for the number.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#         else:
#             choice = input("Do you want to check another number? (y/n): ").strip().lower()
#             if choice != "y":
#                 print("Program Completed.")
#                 break
# main()

# srys = 1000

# for sry in range (1, srys + 1):
#     print ("Sorry Baby")

"""
Arithmetic Operations:
Addition (+): Adds two numbers together.
Subtraction (-): Subtracts one number from another.
Multiplication (*): Multiplies two numbers.
Division (/): Divides one number by another.
Comparison Operations:
Floor Division (//): Divides one number by another and returns the largest integer less than or equal to the result.
Modulus (%): Returns the remainder of a division operation.
Power (**): Raises a number to the power of another number.
"""
# using addition
num1 = 10
num2 = 5

print (num1 + num2) 