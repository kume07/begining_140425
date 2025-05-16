def introduce_person(name: str, age: int) -> str:
    assert isinstance(name, str) and name.strip() != ""
    assert isinstance(age, int) and age > 0
    return f"Hi. My name is {name} and I am {age}."


name = input("Your name: ")
age = int(input("Your age: "))

print(introduce_person(name, age))
