import re


def is_palindrome(some_text: str) -> bool:

    processed_string = re.sub(r"[^a-zA-Z0-9]", "", some_text).lower()
    return processed_string == processed_string[::-1]


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
