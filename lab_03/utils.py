import csv
from student import Student

class Utils:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        students = []
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(Student(row["name"], row["phone"], row["email"], row["group"]))
        return students

    def save_data(self, students):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "group"])
            writer.writeheader()
            for s in students:
                writer.writerow({
                    "name": s.name,
                    "phone": s.phone,
                    "email": s.email,
                    "group": s.group
                })