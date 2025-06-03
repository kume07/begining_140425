import re
import codecs


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    # Видаляємо всі HTML-теги за допомогою регулярного виразу
    cleaned_text = re.sub(r"<[^>]+>", "", html)

    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(cleaned_text)


delete_html_tags("draft.html", "cleaned.txt")
