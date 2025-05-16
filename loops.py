from pprint import pprint

some_list = [55, 222] * 6
some_string = "23343ggfgfgdf"
products = ["banana", "vodka", "milk", "bread", "vodka"]
# products = []

for product in products:

    if product == "milk":
        break

    if product == "vodka":
        continue

    print(product)
    if product == "vodka":
        print("No boooze today")

# print(product)
print(1234)

people = [
    ["JJ", "Mclean", "Florida", 43, True],
    ["Pitt", "Brad", "Chicago", 55, False],
    ["Alex", "Carter", "Texas", 77, False],
    ["John", "BonJovi", "Texas", 60, False],
    ["Alex", "Bolduin", "Texas", 77, False],
    ["Kevin", "Durant", "Oklahoma", 35, True],
    ["Lebron", "James", "Florida", 40, True],
    ["David", "Becks", "Miami", 49, True],
]
#####################################################################
# all_married_people
# not married from Texas
# average age of married people
# 3 Alex below 22

all_married_people = []
not_married_from_texas = []
city = "Texas"
total_age = 0
people_married = 0

#######################
for person in people:
    # ["David", "Becks", "Miami", 49, True]
    name, surname, address, age, is_married = person

    # is_married = person[4]
    # address = person[2].lower()
    # address = address.lower()
    if is_married:
        # print(person)
        all_married_people.append(person)
    if not is_married and city.lower() in address.lower():
        not_married_from_texas.append(person)

if all_married_people:
    ages = []
    for married_person in all_married_people:
        age = married_person[3]
    total_age += age

    # version 2
    ages.append(age)
    print(f"Average age of married = {total_age/len(all_married_people)}")
    print(f"Average age of married = {sum(ages)/len(all_married_people)}")
else:
    print("No married - no age")
print("all married ")
pprint(all_married_people)
print(f"not all married from {city}")
pprint(not_married_from_texas)

#######################
# for person in people:
# ["David", "Becks", "Miami", 49, True]
#   is_married = person[4]
#    if is_married:
#        # print(person)
#        all_married_people.append(person)
# pprint(all_married_people)


# not married from Texas
# not_married_from_texas = []
# city = "Texas"
# for person in people:
#    is_married = person[4]
#    address = person[2].lower()
#    if not is_married and city.lower() in address:
#        not_married_from_texas.append(person)
# pprint(not_married_from_texas)

# average age of married people
#
