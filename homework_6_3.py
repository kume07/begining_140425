def multiply_digits_until_single_digit(number):
    while number > 9:
        item = 1
        for digit in str(number):
            item *= int(digit)
        number = item
    return number


user_input = int(input("Please enter your number: "))
result = multiply_digits_until_single_digit(abs(user_input))
print("Your result:", result)
