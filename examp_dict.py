from pprint import pprint

# creation
user = {
    "id": 22,
    "name": "Alex",
    "hobbies": ["tennis", "soccer"],
    "is_married": True,
    "address": {
        "city": "Odesa",
        "street": "Derybasivska",
        "building": 15,
    },
    "siblings": None,
    "money": 100,
    0: 555,
}
user2 = dict(id=365, name="John")
user3 = dict(id=3655, name="Marta", hobbies=None)

parcel = {}
parcel2 = dict()
raw_data_for_dict = [[5, 8], ["a", "a"]]
parcel3 = dict(raw_data_for_dict)
pass

scores = {0: ["Alex"], 20: ["Marta", "John"], None: ["Alex2"]}

# get data
# user_id = user["id"]
# user2_id = user2["id"]
#
# user_hobbies = user.get("hobbies", [])
# user2_hobbies = user2.get("hobbies", [])
# user3_hobbies = user3.get("hobbies") or []

# for hobby in user_hobbies:
#     print(f"user hobby - {hobby}")
#
# for hobby2 in user2_hobbies:
#     print(f"user2 hobby - {hobby2}")

# update
# list type
# user2["hobbies"] = ["diving"]
# user2["hobbies"] = ["scuba"]
# user2["hobbies"].append("diving")
#
# # int type
# user["money"] += 200
#
# # dict type
# user["address"]["city"] = "Lviv"
# user["address"]["street"] = "Hvylovogo"
#
# pprint(user, indent=4)

#
user_address = {
    "city": "Odesa",
    "street": "Derybasivska",
    "building": 15,
}
user_data = {"id": 18, "city": "Kyiv"}

result_dict_option1 = {**user_address, **user_data}
result_dict_option2 = user_address | user_data

# print(result_dict_option2 == result_dict_option1)

# delete
# delete all data in dict
result_dict_option1.clear()

# delete value by key
del result_dict_option2["street"]
city = result_dict_option2.pop("city2", "")


# iterate
# for elem in user:
#     print(elem, "->", user[elem])

my_tuple = (5, 6, 5)
print(my_tuple.count(5))
print(my_tuple.index(5, 2))

# my_tuple2 = "key", "value"
# key, value = my_tuple2


my_tuple3 = ("data",)

l = [
    "dfghfdg",
    "dfgfdgfdgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg,"
    "dfgdfgdfgdf",
]

for key, value in user.items():
    print(key, value)

# atlethes = []
# for elem in scores.values():
#     atlethes.extend(elem)
# print(atlethes)
