# some_string = "I live in Odesa since 2004/"
# #
# # other_result = some_string.split("i")
# # other_result_visual = ["I", "live", "in", "Odesa", "since", "2004"]
#
# empty_list = []
#
# if empty_list:
#     print(555555555555)
#
# not_empty_list = ["4545", 5555, 5.5, True, False, [55], empty_list]
# if not_empty_list:
#     print(222222222222)
#
# fifth_elem = not_empty_list[4]
# # big_elem = not_empty_list[40]
# fifth_letter = some_string[4]
#
# len_list = len(not_empty_list)
# len_list2 = len(empty_list)
# len_string = len(some_string)
#
# pass

purchase_plan = ["banana"]

# add 1 elem
purchase_plan.append("salt")
purchase_plan.append("salt")
purchase_plan.append("2")
purchase_plan.append("")

# merge by another list
sister_plan = ["bread", "milk"]
purchase_plan.extend(sister_plan)
# purchase_plan.extend("5656dfgfdg5656")

purchase_plan.sort()
# purchase_plan.sort(reverse=True)
# purchase_plan.sort(key=len, reverse=True)


# delete item
purchase_plan.remove("salt")

if "nails" in purchase_plan:
    purchase_plan.remove("nails")

if "abc" in "abcdd":
    print(32323232)


# delete by index
last_elem = purchase_plan.pop()
purchase_plan.pop(0)
pass

purchase_plan.insert(1, 55555555555555555)
pass
