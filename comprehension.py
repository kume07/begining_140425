import sys

source_list = [3, 5, "gfgfdss", True, "data", [], 5.5]

# list comprehension

# result_only_numbers = [item for item in source_list if type(item) in [int, float]]
result_numbers_x_2 = [
    item * 2 for item in source_list if isinstance(item, (int, float))
]
result_with_true_false = True + False + True + 55
# set comprehension
set_result_1 = set(result_numbers_x_2)
set_result_2 = {number for candidate in source_list if isinstance(int, float)}


# dict comprehension
dict_result_1 = {number: number for number in result_numbers_x_2}

# comprehension
result_generator = (
    candidate for candidate in source_list if isinstance(candidate, (int, float))
)

# print(sys.getsizeof(source_list))
# print(sys.getsizeof(result_numbers_x_2))

print(next(result_generator))
print(next(result_generator))
print(next(result_generator))
# list_from_generator = list(result_generator)
# for item in result_generator:
#     print(item)

pass
