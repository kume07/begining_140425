class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name} (${self.price}) per kg - {self.description}, size: {self.dimensions}"


class User:

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, Phone: {self.phone_number}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt
        self.total += item.price * cnt

    def __str__(self):
        items_str = "\n".join(
            [
                f"{item.name} x {cnt} kg = {item.price * cnt}$"
                for item, cnt in self.products.items()
            ]
        )
        return f"Purchase for {self.user}:\n{items_str}\nTotal: {self.total}$"

    def get_total(self, currency="USD", rate=42):
        if currency == "USD":
            return round(self.total, 2)  # сума в доларах
        elif currency == "UAH":
            return round(self.total * rate, 2)  # конвертація у гривні
        else:
            raise ValueError


kiwi = Item(
    "kiwi",
    2.0,
    "ripe and ready to eat",
    "middle",
)
apple = Item(
    "apple",
    1.5,
    "sweet and juicy",
    "middle",
)
print(kiwi)
print(apple)

buyer = User("Oleksii", "K.", "073XXXXXXX")
print(buyer)

cart = Purchase(buyer)
cart.add_item(kiwi, 1)
cart.add_item(apple, 1)
print(cart)
print("Total in USD:", cart.get_total("USD"))  # 3.5$
print("Total in UAH:", cart.get_total("UAH"))

assert isinstance(cart.user, User) is True, "Екземпляр класу User"

cart.add_item(apple, 5)
print(cart)

assert cart.get_total() == 11
