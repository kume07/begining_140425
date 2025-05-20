def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}

    common = multiples_of_3 & multiples_of_5
    return common


print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Super")
