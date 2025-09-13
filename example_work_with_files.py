# my_file = open("game.py")
# my_file.close()
from homework_4_3 import numbers

# only reading
# with open("game.py", mode="r", encoding="utf-8") as file:
#     content = file.read()
# print(content)

# writting
with open("shop_plan.txt", mode="a", encoding="utf-8") as file:
    for position in range(1, 10, +1):
        file.write(f"data:{position}\n")
    file.write("the end\n")
