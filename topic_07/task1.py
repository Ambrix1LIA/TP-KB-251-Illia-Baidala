class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"


students = [
    Student("Олександр", 19),
    Student("Анна", 18),
    Student("Ілля", 18),
    Student("Дмитро", 20),
    Student("Богдан", 19),
]

print("Початковий список студентів:")
for s in students:
    print(s)

sorted_by_name = sorted(students, key=lambda s: s.name)
print("\nСортування за ім'ям:")
for s in sorted_by_name:
    print(s)

sorted_by_age = sorted(students, key=lambda s: s.age)
print("\nСортування за віком:")
for s in sorted_by_age:
    print(s)