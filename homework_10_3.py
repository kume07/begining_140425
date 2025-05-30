def is_even(number) -> bool:
    return number % 2 == 0


assert is_even(2) == True, "Test1"
assert is_even(5) == False, "Test2"
assert is_even(0) == True, "Test3"
print("OK")
