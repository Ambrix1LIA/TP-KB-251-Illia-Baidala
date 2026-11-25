from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        pos = 0
        for s in self.students:
            if student.name.lower() > s.name.lower():
                pos += 1
            else:
                break
        self.students.insert(pos, student)

    def delete_student(self, name):
        for i in range(len(self.students)):
            if self.students[i].name.lower() == name.lower():
                del self.students[i]
                return True
        return False

    def update_student(self, old_name, new_name, phone, email, group):
        for i in range(len(self.students)):
            if self.students[i].name.lower() == old_name.lower():
                del self.students[i]
                new_student = Student(new_name, phone, email, group)
                self.add_student(new_student)
                return True
        return False

    def print_all(self):
        print("-" * 60)
        for s in self.students:
            print(s)
        print("-" * 60)