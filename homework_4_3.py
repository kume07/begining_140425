numbers = [4, 99, 2, 77]
new_lst = [numbers[0], numbers[2], numbers[-2]]
print(new_lst)

# або

numbers = [4, 77, 21, 99, 88]

if len(numbers) >= 3 and len(numbers) <= 10:
    new_lst = [numbers[0], numbers[2], numbers[-2]]
    print("Новий список:", new_lst)
else:
    print("У списку має бути від 3 до 10 елементів.")
