# Step 1: Accept two Boolean values
val1 = input("Enter first value (True/False): ")
val2 = input("Enter second value (True/False): ")

# Step 2: Convert string inputs to actual Boolean values
# (so "True" becomes True, "False" becomes False)
val1 = True if val1 == "True" else False
val2 = True if val2 == "True" else False

# Step 3: Display logical operation results
print("AND:", val1 and val2)
print("OR:", val1 or val2)
print("NOT First Value:", not val1)