lst = [0, 5, 77, 0, 0, 21, 66]
all_zero_in_the_end = []  # створюємо новий список згідно завданню

for item in lst:  # перебираємо список для чисел
    if item != 0:
        all_zero_in_the_end.append(item)

for item in lst:  # перебираємо список для нулів
    if item == 0:
        all_zero_in_the_end.append(0)

print(all_zero_in_the_end)
