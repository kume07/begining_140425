def introduce_person(name: str, age: int) -> str:
    return f"Hi. My name is {name} and I am {age}."


name = input("Your name: ")
age = int(input("Your age: "))

print(introduce_person(name, age))
