import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    @staticmethod
    def make_rectangle_with_area(area):
        for i in range(int(math.sqrt(area)), 0, -1):
            if area % i == 0:
                return Rectangle(i, area // i)
        return Rectangle(1, area)

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area = self.get_square() + other.get_square()
        return Rectangle.make_rectangle_with_area(new_area)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = int(self.get_square() * n)
        return Rectangle.make_rectangle_with_area(new_area)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height}) = {self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, "Test1"
assert r2.get_square() == 18, "Test2"

r3 = r1 + r2
assert r3.get_square() == 26, "Test3"

r4 = r1 * 4
assert r4.get_square() == 32, "Test4"

assert Rectangle(3, 6) == Rectangle(2, 9), "Test5"
