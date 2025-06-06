class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        self.current = current

    def set_current(self, start: int) -> None:
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError(
                "Початкове значення повинно бути між мінімумом та максимумом"
            )

    def set_max(self, i_max: int) -> None:
        if i_max < self.min_value:
            raise ValueError("Максимум не може бути меншим за мінімум")
        self.max_value = i_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, i_min: int) -> None:
        if i_min > self.max_value:
            raise ValueError("Мінімум не може бути більшим за максимум")
        self.min_value = i_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self) -> None:
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максимуму")

    def step_down(self) -> None:
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімуму")

    def get_current(self) -> int:
        return self.current


# Тестування:
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, "Test1"

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Досягнуто максимуму

assert counter.get_current() == 10, "Test2"

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, "Test3"

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Досягнуто мінімуму

assert counter.get_current() == 7, "Test4"
