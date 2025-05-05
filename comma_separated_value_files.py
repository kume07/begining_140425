import random
import csv
from os import write

products = ["bread", "milk", "ice_cream", "salat"]

# with open("shop_plan.csv", mode="+a", encoding="utf-8") as file:
#     if not file.read().strip():
#         file.write("Product; quantity\n")
#     for position in products:
#         file.write(f"{position}; {random.randint(1, 50)}\n")

with open("shop_plan.csv", mode="a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    for product in products:
        writer.writerow([product, random.randint(1, 52)])

with open("shop_plan.csv", mode="r", encoding="utf-8") as file:
    # for line in file.readlines():
    #     print(line, end="")
    reader = csv.reader(file)
    for row in reader:
        print(row)
