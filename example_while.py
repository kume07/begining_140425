TARGET_COUNTER = 3

flag = True
counter = 0

# while flag:
#     print(111)
#     counter += 1
#     if counter == TARGET_COUNTER:
#         flag = False
#         print("by")


# while counter != TARGET_COUNTER:
#     print(111)
#
#     counter += 10

# while counter <= TARGET_COUNTER:
#     print(111)
#     counter += 1

while True:
    counter += 1
    if counter == 2:
        continue
    print(111)
    if counter >= TARGET_COUNTER:
        break
