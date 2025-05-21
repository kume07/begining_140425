import random


def create_and_extract_list() -> []:
    """
    Створює список випадкових чисел, витягує з нього 3 елементи та повертає новий список.

    Returns:
        list: Новий список, що містить 3 елементи: перший, третій і другий з кінця початкового списку.
              Повертає None, якщо довжина початкового списку менша за 3.
    """

    # Створюємо випадкову довжину списку від 3 до 10
    list_length = random.randint(3, 10)

    # Створюємо список випадкових чисел (від 1 до 100 для прикладу)
    original_list = [random.randint(1, 100) for _ in range(list_length)]

    # Перевіряємо, чи достатньо елементів для вибірки
    if len(original_list) < 3:

        return None  # або викликати виняток, залежно від необхідності

    # Створюємо новий список з вибраних елементів
    new_list = [original_list[0], original_list[2], original_list[-2]]
    print("Початковий список:", original_list)
    print("Список з вибраними елементами:", new_list)

    return new_list


create_and_extract_list()
