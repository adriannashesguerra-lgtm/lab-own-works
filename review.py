# output operators
print("HELLO WORLD")

# inserting \n
print("\nHello\nWorld")

print("i dont know what to do,\t"
      "same to you?")

# using end in print
print("What if", end = ', ' 
      "you have another reason for you to live more?")

# using print for a formatted output
num1 = 'True'
num2 = 'False'

num1 = True if num1 == 'True' else False
num2 = True if num2 == 'True' else False

print(f"the boolean value of num1 and num2 is: {num1 and num2}")
print (f"{num1} and {num2} = {num1 and num2}")

# using basic escape sequences
""" 
\n = adding a new line in the code
\t = adding a horizontal tab
\b = removing a horizontal tab (a backspace)
\" = inserting a double quote
\' = inserting a single quote
\\ = inserting a backslash character
"""
print("This is a new line: \nwow")
print("Hello\tworld")
print("\"wow\"")
print("\'amen\'")
print("oh \bmy \bgod")
print("\\wazup\\")

# using place holders
name = input("what is your complete name?\t").strip().title()
age = int(input("How old are you?\t"))

print(f"Complete name:\t{name}\nAge:\t{age}")

# using format specifiers
"""
%d = signed integer
%f = floating-point number
%s = string
%c = for a single string character
"""
age = 18
height = 1.60
grade = 'A'
name = input("what is your first name?\t").strip().title()

print("Age: %d" % age)
print("Height: %.2f meters" % height)
print("Grade: %c" % grade)
print("Name: %s" %name)

# input operations
"""
input() = getting users response
int() = converting string output of input into a string
float() = converting string output of input into a float 
list(map()) = for making lists
bool() = for true or false
"""
grade_level = input("what is your current grade level? ").strip().title()
num1 = int(input("WHat is the value of the first number: "))
num2 = float(input("What is the value of the second number: "))
lists = list(map(int, input("Enter five integer numbers with spacing: ").split()))
bools = bool(input("Enter a boolean value [True or False]"))
bools = True if bools == 'True' or 'true' else False
print(f"Level:\t{grade_level}\nNum1:\t{num1}"
      f"\nNum2:\t{num2}\nLists:\t{lists}\nBool:\t {bools}")

# arithmetic operators
"""
+ = addition
- = subtraction
* = multiplication
/ = division
% = modulus
// = floor division
** = exponentiation
"""
num1 = int(input("num1:\t"))
num2 = int(input("num2:\t"))

sum = num1 + num2
diff = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2

print(f"Addition: {sum}\nSubtraction: {diff}\nMultiplication: {mul}"
      f"\nDivision: {div}\nModulus: {mod}\nExponentiation: {exp}")

# assignment operators
a = 1 # basic assignment operator
print(f"A: {a}") 

# compound operators
num = 5
num += 4 # equals to num + 4 = num
print(f"Num: {num}")

numb = 10
numb -=8 # equals to numb - 8 = numb
print(f"Num: {numb}")

numbe = 12
numbe *=12 # equals to numbe * 12 = numbe
print(f"Num: {numbe}")

number = 133
number /= 10 # equals to number / 10 = number
print(f"Num: {number}")

numbers = 144
numbers %= 10 # equals to numbers % 10 = numbers
print(f"Num: {numbers}")

numberss = 111
numberss //= 5 # equals to numberss // 5 = numberss
print(f"Num: {numberss}")

numbersss = 100
numbersss **= 16 # equals to numbersss ** 16 = numbersss
print(f"Num: {numbersss}")

# bitwise operators
num1 = 10    # Binary: 0000 1010
num2 = 6     # Binary: 0000 0110
	
result = num1 & num2     # Bitwise AND: 0000 0010 (2 in decimal)
print("AND Result:", result)
	
result = num1 | num2     # Bitwise OR: 0000 1110 (14 in decimal)
print("OR Result:", result)
	
result = num1 ^ num2     # Bitwise XOR: 0000 1100 (12 in decimal)
print("XOR Result:", result)

result = ~num1           # Bitwise complement: 1111 0101 (245 in decimal)
print("Complement Result:", result)

result = num1 << 2       # Left shift by 2: 0010 1000 (40 in decimal)
print("Left Shift Result:", result)

result = num2 >> 1       # Right shift by 1: 0000 0011 (3 in decimal)
print("Right Shift Result:", result)

# string handling
name = input("Enter your name: ") #string input
print(f"Hello, {name}!")

str1 = "Hello"
str2 = "World"

concatenated_str = str1 + str2 # string concentrated
print("Concatenated string:", concatenated_str)

# Using f-string (formatted string literals)
name = "John"
greeting = f"Hello, {name}!"
print(greeting)

str1 = "banana"
str2 = "mango"

result = str1 == str2 # string comparison
print(result)  # Output will be True

str1 = "Hello"
str2 = str1

print("Copied string:", str2) # string copying

# type casting
x = 10
y = 3.14
result = x + y  # Implicit typecasting from int to float

print(result)  # Output: 13.14

# explicit typecasting
"""
int() = converts value into an integer
float() = converts value into a float
str() = converts value into a string
chr() = converts value into a character
"""

x = 65
y = str(x)  # Explicitly casting int to string
print(y)

a = "3.14"
b = float(a)  # Explicitly casting string to float
print(b)

p = 100
q = int(p)  # Explicitly casting int to int (no change, but it can be useful in certain contexts)
print(q)

x = 65
y = chr(x)  # Explicit typecasting from int to char (using the chr() function)
print(y) 

# pre-defined String Functions/Methods
"""
len() = for determining the length of the string
str.replace() = for replacing occurrences of a substring in a string with a new substring
str.strip() = to remove leading and trailing whitespace characters (such as spaces and tabs) from a string
str.join() = to join elements of an iterable (such as a list) into a single string
str.startswith() and str.endswith() = to check if a string starts or ends with a specified prefix or suffix
str.find() and str.rfind() = to find the first occurrence of a substring in a string
str.index() and str.rindex() = to find the first occurrence of a substring in a string
"""
# standard string methods
str = "Hello, World!"
length = len(str)
print("Length of the string:", length)

str = "Hello, World!"
new_str = str.replace("World", "Python")
print("Modified string:", new_str)

str = "   Hello, World!   "
new_str = str.strip()
print("Stripped string:", new_str)

words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print("Joined sentence:", sentence)

str = "Hello, World!"

starts_with_hello = str.startswith("Hello")
ends_with_world = str.endswith("World")
print("Starts with 'Hello':", starts_with_hello)
print("Ends with 'World!':", ends_with_world)

# string finding operations
str = "Hello, World!"

first_occurrence = str.find("l")
last_occurrence = str.rfind("l")
print("First occurrence of 'l':", first_occurrence)
print("Last occurrence of 'l':", last_occurrence)

str = "Hello, World!"

first_occurrence = str.index("l")
last_occurrence = str.rindex("l")
print("First occurrence of 'l':", first_occurrence)
print("Last occurrence of 'l':", last_occurrence)

# relational operators
"""
== = equals to
!= = not equals to
> = greater than
< = less than
"""

a = 10
b = 20

equal = (a == b)  # The `==` operator compares the values of `a` and `b`
print("Are `a` and `b` equal?", equal)

number = 10

not_zero = (number != 0)  # The `!=` operator checks if `number` is not equal to zero
print("Is the number not zero?", not_zero)

x = 5
y = 10

greater = (x > y)  # The `>` operator compares the values of `x` and `y`
print("Is x greater than y?", greater)

x = 6
y = 10

lesser = (x < y)  # The `<` operator compares the values of `x` and `y`
print("Is x greater than y?", lesser)

# boolean operators
"""
and = returns True if both of its operands are True, and False otherwise
or  = returns True if at least one of its operands is True, and False otherwise
not = reverses the logical state of its operand. If the operand is True, the not operator returns False, and if the operand is False, it returns True
"""
age = 25
day = 1

answer = (age > 20 and day > 0)  # answer = True
print (answer)

score = 80

answer1 = (score >= 90 or score <= 50)  # answer = False
print(answer1)

x = 5
y = 10

answer2 = not (x > y)  # answer = True
print(answer2)

# use pf short circuit evaluation
x = 5
y = 10

answer3 = (x > 0 and y / x > 2)  # answer = False
print(answer3)

# if, if-else, if-elif-else statement and nested decision
""""
if = evaluates to either True or False
if-else = evaluates to either True or False. if the condition is True, the code block indented under the if statement will be executed.
            if the condition is False, the code block indented under the else statement will be executed
if-elif-else = evaluates to either True or False. The if clause checks the first condition, and if it is True, the corresponding code block is executed. 
                if the first condition is False, the program moves to the next elif clause and evaluates its condition. 
                this process continues until a condition is found to be True, in which case the corresponding code block is executed. 
                if none of the conditions are True, the code block within the else clause is executed
nested = practice of placing one or more if...else statements inside another if or else block
"""
# if example
age = 20

if age >= 18:
    print("You are an adult.")

# if-else example
print ("Welcome to the ticket website")
age = int(input("How old are you? "))
amount = int(input("Enter how many would you like to purchase [price = 150]? "))
price = amount * 150
#calculate
if age <= 12 or age >= 60:
    dsic = 0.20
    fprice = price - (price * dsic)
    discount = "Yes"
else:
    fprice = price
    discount = "No"

#display the receipt
print ("\n===Cinema Ticket Checkout===")
print (f"Age: {age}")
print (f"Tickets: {amount}")
print (f"\n---Receipt---")
print (f"Initial price: {price}")
print (f"Discount applied: {discount}")
print (f"Final price: {fprice}")

    
# if-elif-else example
num = 5
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("Invalid number.")
    
# nested decision
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
    
# rounding off numbers using round and f string
x = float(input("Value 1: "))
y = float(input("Value 2: "))

ans = round(x + y, 2)
anss = x + y
print(ans)
print(f"{anss:.2f}")

# defining your function
def hello(to):
    print("hello,", to)

name = input("Enter your name: ")
hello(name)

def hello(to="world"):
    print("hello,", to)

name = input("Enter your name: ")
hello(name)
hello()

def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

# return function
def main():
    x = int(input("Enter a number: "))
    print("x squared is:", square(x))

def square(x):
    return pow(x, 2)

main()

num = 1

while num <= 5:
    print(num)