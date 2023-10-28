def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Enter option")
    print("'add', 'subtract', 'multiply', 'divide', 'exit'")

    option = input("")

    if option == "exit":
        break
    elif option in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == "add":
            print("Result:", add(num1, num2))
        elif option == "subtract":
            print("Result:", subtract(num1, num2))
        elif option == "multiply":
            print("Result:", multiply(num1, num2))
        elif option == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")