def correct_text(text: str) -> str:
    if not text:
        return ""

    corrected = text[0].upper() + text[1:]

    if not corrected[-1] in ".!?":
        corrected += "."

    return corrected


print(correct_text("hello. what's up?"))  # Очікування: Hello. what's up?

assert correct_text("hello. what's up?") == "Hello. what's up?"
