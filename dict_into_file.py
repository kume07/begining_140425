import json

user = {
    "id": 22,
    "name": "Олександр",
    "hobbies": ["tennis", "soccer"],
    "is_married": True,
    "address": {"city": "Odesa", "street": "Derybasivska", "building": 15, 5: 25},
    "siblings": None,
    "money": 100,
    0: 555,
}

# dict to string
result_string = json.dumps(user, ensure_ascii=False)

# string to dict
recover_dict = json.loads(result_string)

# dict to file
with open("user.json", mode="w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)
    # json.dump(user, file, indent=4, ensure_ascii=False)

# file into dict
with open("user.json", mode="r", encoding="utf-8") as file:
    decover_from_file = json.load(file)
    pass