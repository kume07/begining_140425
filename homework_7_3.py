def second_index(text: str, target: str) -> int | None:
    first = text.find(target)
    if first == -1:
        return None
    second = text.find(target, first + 1)
    return second if second != -1 else None


assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"
assert second_index("Just do it!", "t") == 9, "Test5"
print("ОК")
