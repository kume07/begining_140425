numbers = int(input('Enter any 4 numbers:'))

number1 = numbers // 1000
number2 = (numbers // 100) % 10
number3 = (numbers // 10) % 10
number4 = numbers % 10

print(number1)
print(number2)
print(number3)
print(number4)