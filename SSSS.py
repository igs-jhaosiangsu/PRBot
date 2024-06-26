def subtract_numbers(a, b):
    """Return the difference between two numbers."""
    return a - b

def main():
    print("Simple Subtraction Program")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = subtract_numbers(num1, num2)
    
    print(f"The difference between {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
