import sys
import csv

students = []

def load_data(filename):
    global students
    students.clear()
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)

def save_data(filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "group"])
        writer.writeheader()
        writer.writerows(students)

def add_student(name, phone, email, group):
    new_item = {"name": name, "phone": phone, "email": email, "group": group}
    pos = 0
    for s in students:
        if name > s["name"]:
            pos += 1
        else:
            break
    students.insert(pos, new_item)
    return pos

def delete_student(name):
    for i in range(len(students)):
        if students[i]["name"] == name:
            del students[i]
            return True
    return False

def update_student(old_name, new_name, phone, email, group):
    for i in range(len(students)):
        if students[i]["name"] == old_name:
            del students[i]
            add_student(new_name, phone, email, group)
            return True
    return False

def print_all():
    print("-" * 60)
    for s in students:
        print(s["name"] + " | " + s["phone"] + " | " + s["email"] + " | " + s["group"])
    print("-" * 60)

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "lab2.csv"
    load_data(filename)

    while True:
        choice = input("[ C create, U update, D delete, P print, X exit ]: ")
        if choice in ("C", "c"):
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            group = input("Group: ")
            add_student(name, phone, email, group)
        elif choice in ("U", "u"):
            old_name = input("Enter name to update: ")
            name = input("New name: ")
            phone = input("New phone: ")
            email = input("New email: ")
            group = input("New group: ")
            update_student(old_name, name, phone, email, group)
        elif choice in ("D", "d"):
            name = input("Enter name to delete: ")
            delete_student(name)
        elif choice in ("P", "p"):
            print_all()
        elif choice in ("X", "x"):
            save_data(filename)
            print("Exit()")
            break

if __name__ == "__main__":
    main()