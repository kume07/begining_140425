def find_unique_value(some_list):
    for element in some_list:
        if some_list.count(element) == 1:
            return element


assert find_unique_value([4, 6, 33, 21, 6, 33]) == 4, "Test1"
assert find_unique_value([33, 8, 6, 33, 77, 6, 8]) == 77, "Test2"
assert find_unique_value([33, 6, 33, 21, 6]) == 21, "Test3"
print("ОК")