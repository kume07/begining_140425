lst = [3, 7, 4, 1, 2]

def special_sum(lst):
    if not lst:
        return 0
    sum_at_index_0_2_4 = sum(lst[::2])
    return sum_at_index_0_2_4 * lst[-1]

print(special_sum(lst))
