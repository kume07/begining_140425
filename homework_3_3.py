def split_list(any_list):
    midlle = (len(any_list) + 1) // 2
    # Розділяємо список на два списки. Якщо кількість непарна, перший список буде більшим
    return [any_list[:midlle], any_list[midlle:]]
