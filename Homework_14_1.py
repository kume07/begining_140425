class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()} Record Book: {self.record_book}"


class GroupLimitError(Exception):
    def __init__(self, message="Неможливо додати більше 10 студентів до групи"):
        super().__init__(message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


# Тестування
students = [
    Student("Male", 20, "Gareth", "Bale", "RB001"),
    Student("Male", 21, "Wayne", "Rooney", "RB002"),
    Student("Male", 22, "David", "Beckham", "RB003"),
    Student("Male", 23, "Mike", "Owen", "RB004"),
    Student("Male", 23, "Cole", "Palmer", "RB004"),
    Student("Male", 24, "John", "Davis", "RB005"),
    Student("Male", 26, "Declan", "Rice", "RB007"),
    Student("Male", 27, "Roy", "Kean", "RB008"),
    Student("Male", 28, "Bobbie", "Robson", "RB009"),
    Student("Male", 29, "Andy", "Cole", "RB010"),
    Student("Male", 30, "Ashley", "Cole", "RB011"),  # 11-й студент
]

gr = Group("PD1")

for student in students:
    try:
        gr.add_student(student)
    except GroupLimitError as e:
        print(f"❌ Помилка: {e}")

print(gr)

assert (gr.find_student("Davis")) == students[5], "Test1"
student = gr.find_student("Jobs")
assert student is None, "Test2"

gr.delete_student("Kean")
print(gr)
print("Roy Kean has been deleted")

gr.delete_student("Kean")  # No error!
