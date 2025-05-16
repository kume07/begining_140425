def calculator():
    while True:
        number_1 = float(input("Enter your number: "))
        operator = input("Operation (+, -, *, /): ")
        number_2 = float(input("Enter your second number: "))

        if operator == "+":
            result = number_1 + number_2
        elif operator == "-":
            result = number_1 - number_2
        elif operator == "*":
            result = number_1 * number_2
        elif operator == "/":
            if number_2 == 0:
                print("Attention! You made mistake. Division by zero is not allowed")
                continue
            result = number_1 / number_2
        else:
            print("Unknown operation.")
            continue

        print(f"Result: {result}")

        cont = input("Would you like to continue? (y/yes): ").strip().lower()
        if cont not in ("y", "yes"):
            print("The end.")
            break


calculator()
