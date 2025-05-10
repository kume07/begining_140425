import string


def convert_to_hashtag():
    text = "So, it's my homework 5.3"

    # Видаляємо символи та пробіли
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator)

    # Ділимо наш текст на слова, та перетворюємо кожне з великої літери
    words = cleaned_text.split()
    capitalized_words = [word.capitalize() for word in words]

    # Додаємо хештег
    hashtag = "#" + "".join(capitalized_words)

    # Встановлюємо ліміт до 140 символів
    return hashtag[:140]


print(convert_to_hashtag())
