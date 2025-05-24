def popular_words(text: str, words: list) -> dict:
    text = text.lower().split()
    result = {}
    for word in words:
        result[word] = text.count(word)
    return result


our_text = "When I was One I had just begun When I was Two I was nearly new"
words_to_count = ["i", "was", "three", "near"]

print(popular_words(our_text, words_to_count))
