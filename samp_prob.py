def factorial(num):
    result = 1
    
    if num == 0:
        return 1
    
    if num < 0:
        return "Factorial is not defined for negative numbers."
    
    for i in range(1, num + 1):
        result *= i
    return result

def main ():
    num = int(input("Enter a number: "))
        
    res = factorial(num)
        
    print(f"The factorial of {num} is: {res}")
        
main()