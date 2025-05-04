def simple_calculator():
    num_1 = float(input("Enter your first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num_2 = float(input("Enter your second number: "))

    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        if num_2 == 0:
            print("Error: operation not possible!")
            return
        result = num_1 / num_2
    else:
        print("Error")
        return

    print(f"Result: {result}")


simple_calculator()
