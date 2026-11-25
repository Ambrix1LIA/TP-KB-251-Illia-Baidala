import sys
from student import Student
from student_list import StudentList
from utils import Utils

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "lab3.csv"
    file_manager = Utils(filename)

    group_list = StudentList()
    for s in file_manager.load_data():
        group_list.add_student(s)

    while True:
        choice = input("[ C create, U update, D delete, P print, X exit ]: ")
        if choice in ("C", "c"):
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            group = input("Group: ")
            group_list.add_student(Student(name, phone, email, group))
        elif choice in ("U", "u"):
            old_name = input("Enter name to update: ")
            name = input("New name: ")
            phone = input("New phone: ")
            email = input("New email: ")
            group = input("New group: ")
            group_list.update_student(old_name, name, phone, email, group)
        elif choice in ("D", "d"):
            name = input("Enter name to delete: ")
            group_list.delete_student(name)
        elif choice in ("P", "p"):
            group_list.print_all()
        elif choice in ("X", "x"):
            file_manager.save_data(group_list.students)
            print("Exit()")
            break

if __name__ == "__main__":
    main()