import re
import codecs


def delete_html_tags(html_file, result_file="cleaned.txt") -> None:
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    cleaned_text = re.sub(r"<[^>]+>", "", html)

    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(cleaned_text)


delete_html_tags("draft.html", "cleaned.txt")
