from students import Student
from group_st import Group, GroupLimitError

# Студенти
students = [
    Student("Male", 20, "Gareth", "Bale", "RB001"),
    Student("Male", 21, "Wayne", "Rooney", "RB002"),
    Student("Male", 22, "David", "Beckham", "RB003"),
    Student("Male", 23, "Mike", "Owen", "RB004"),
    Student("Male", 23, "Cole", "Palmer", "RB005"),
    Student("Male", 24, "John", "Davis", "RB006"),
    Student("Male", 26, "Declan", "Rice", "RB007"),
    Student("Male", 27, "Roy", "Kean", "RB008"),
    Student("Male", 28, "Bobbie", "Robson", "RB009"),
    Student("Male", 29, "Andy", "Cole", "RB010"),
    Student("Male", 30, "Ashley", "Cole", "RB011"),  # 11-й студент
]

# Створення групи
gr = Group("PD1")

# Додавання студентів
for student in students:
    try:
        gr.add_student(student)
    except GroupLimitError as e:
        print(f"❌ Помилка: {e}")

print(gr)

st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
# gr = Group("PD1") # Другий варіант - Перезаписуємо групу та додаємо двох студентів
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr) # Результат: два студента
# assert gr.find_student("Taylor") == st2
# assert gr.find_student("Jobs2") is None

gr.delete_student("Kean")
print("\nПісля видалення Kean:")  # У результаті буде 9 студентів
