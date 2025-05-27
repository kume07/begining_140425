import random
from inspect import isgenerator


def some_gen():
    first = random.randint(1, 6)
    yield first
    yield 5


gen = some_gen()

assert isgenerator(gen) == True, "Test1"

result = list(gen)

print("Результат генератора:", result)
print("OK")
