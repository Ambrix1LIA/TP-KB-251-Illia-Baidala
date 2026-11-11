students = [
    {"name": "Олександр", "grade": 85},
    {"name": "Анна", "grade": 95},
    {"name": "Ілля", "grade": 90},
    {"name": "Дмитро", "grade": 74},
    {"name": "Богдан", "grade": 60}
]

print("Початковий список:")
for s in students:
    print(s)

sorted_by_name = sorted(students, key=lambda student: student["name"])
print("\nСортування за ім'ям:")
for s in sorted_by_name:
    print(s)

sorted_by_grade = sorted(students, key=lambda student: student["grade"])
print("\nСортування за оцінкою:")
for s in sorted_by_grade:
    print(s)