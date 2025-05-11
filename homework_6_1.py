import string


def letters_range():
    user_input = input("Please, enter two letters (for example: a-f): ")
    start_letter, end_letter = user_input.split("-")

    all_letters = string.ascii_letters

    start_index = all_letters.index(start_letter)
    end_index = all_letters.index(end_letter)

    # усі літери між ними включно
    result = all_letters[start_index : end_index + 1]
    print(result)


letters_range()
