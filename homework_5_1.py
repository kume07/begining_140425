import keyword

# Отримуємо введення користувача
name = input("Enter your word: ")

# Перевірка: чи це коректне ім’я змінної
if name.isidentifier() and not keyword.iskeyword(name):
    print("-> True.")
else:
    print("-> False.")
