def add_one(some_list):
    number = int("".join(str(x) for x in some_list))
    number += 1

    return [int(x) for x in str(number)]


number_input = input("Enter some numbers: -> ")

digits_list = [int(symbol) for symbol in number_input if symbol.isdigit()]

result = add_one(digits_list)

print("Our result:", result)

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
