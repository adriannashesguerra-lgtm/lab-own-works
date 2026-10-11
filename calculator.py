# build a calculator class that can perform basic arithmetic operations
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = a / b
        return self.result

    def clear(self):
        self.result = 0
        
def main():
    calc = Calculator()
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear Result")
        print("6. Exit")

        choice = input("Choose an operation (1-6): ")

        if choice == '6':
            print("Exiting the calculator.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = calc.add(a, b)
                print(f"Result: {result}")
            elif choice == '2':
                result = calc.subtract(a, b)
                print(f"Result: {result}")
            elif choice == '3':
                result = calc.multiply(a, b)
                print(f"Result: {result}")
            elif choice == '4':
                try:
                    result = calc.divide(a, b)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(e)

        elif choice == '5':
            calc.clear()
            print("Result cleared.")
        else:
            print("Invalid choice. Please select a valid operation.")
            
if __name__ == "__main__":
    main()