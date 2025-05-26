from os import pread
from typing import Self

BIRTH_MONEY = 5000


class Person:
    population = []
    DNA = "xyz-fda"

    def __init__(self, given_name: str):
        # print(id(self))
        self.name = given_name.title()
        self.money = BIRTH_MONEY
        self.hobbies = []
        self.population.append(self)

    @property
    def is_poor(self):
        return self.money < 10000

    @staticmethod
    def add_two_numbers(n1, n2):
        return n1 + n2

    def say_hi(self) -> None:
        print(f"I am {self.name}. Hi to me!")

    def __str__(self) -> str:
        return f"<Person with name {self.name}: money >> {self.money}>"

    __repr__ = __str__

    def __del__(self):
        print(f"{self} is dead")

    # def lend_money (self, other: "Person"):
    def lend_money(self, other: Self, amount: int):
        if self.money < amount:
            raise ValueError("No money. Sorry")
        self.money -= amount
        other.money += amount


person1 = Person(given_name="Alex")
person2 = Person(given_name="Spiderman")

print(person1.is_poor)

amount_needed = person1.add_two_numbers(500, 1000)
amount_needed = Person.add_two_numbers(300, 800)

Person.lend_money(self=person1, other=person2, amount=100)
person1.lend_money(person2, amount_needed)

person2.DNA = "BBB-RRR"
print(person1.name)
print(person1.money)
print(person1.hobbies)
print(person1.__dict__)


person1.address = "Odesa"
print(person1.__dict__)

person1.say_hi()
person2.say_hi()

print(person1)
print(person2)

all_persons = Person.population
print(all_persons)
pass
