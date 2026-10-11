# Part A
# problem 1
print("Welcome to Python!"
      "\nProgramming is fun.")

# problem 2
name = input("What is your name? ").strip().title()
course = input("What is your current course? ").strip().title()

print("Student Information\n"
      f"\tName:{name}\n"
      f"\tCourse:{course}")

# problem 3
input1 = 'Hello,'
input2 = 'World!'

print(f"{input1}", end = " ")
print(f"{input2}")

# Part B
# problem 1
first_nm = input("Enter your first name: ").strip().title()
last_nm = input("Enter your last name: ").strip().capitalize()
age = int(input("How old are you? "))

print(f"First name: {first_nm}\nLast name: {last_nm}\nAge: {age}")

# problem 5
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
diff = num1 - num2
pro = num1 * num2
quo = num1 / num2
mod = num1 % num2
floor_div = num1 // num2
exp = num1 ** num2

print("Low key calculator")
print(f"Addition: {sum}\nSubtraction: {diff}\nMultiplication: {pro}\nDivision: {quo}\nModulus: {mod}\nFloor Division: {floor_div}\nExponentiation: {exp}")

# problem 6
numbers = list(map(int, input("Enter a 10 numbers with number spacing: ").split()))

print(f"Numbers: {numbers}")

# problem 7
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}\nPerimeter: {perimeter}")

# problem 8
num = int(input("Enter the value of the first number: "))

square = num ** 2
cube = num ** 3

print(f"Squared: {square}\nCube: {cube}")

# problem 9
minu = int(input("How many minutes did you consume? "))

hours = minu // 60
rem_h = minu % 60

print(f"Hours: {hours:.2f} hours\nRemaining hours: {rem_h} minutes")

# Part D
# problem 10
score1= 75
score2 = 78
score3 = 77

score1 += 10
score2 -= 5
score3 *= 2

print(f"Score 1: {score1}\nScore 2: {score2}\nScore 3: {score3}")

# Part E
# problem 11
name = input("WHat is your name?")

print(f"Number of characters: {len(name)}")
print(f"Upper case version: {name.upper()}")
print(f"Lower case version: {name.lower()}")

# # problem 12
fruit = 'banana'
fruit = 'apple'

print(fruit)