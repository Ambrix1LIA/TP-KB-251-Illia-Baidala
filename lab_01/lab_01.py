globalList = [
    {"name": "Bob", "phone": "0631112233", "email": "bob@gmail.com", "group": "KB-251"},
    {"name": "Emma", "phone": "0632223344", "email": "emma@gmail.com", "group": "KB-251"},
    {"name": "Jon", "phone": "0633334455", "email": "jon@gmail.com", "group": "KB-251"},
    {"name": "Zak", "phone": "0634445566", "email": "zak@gmail.com", "group": "KB-251"},
]


def printAllList(listForPrinting):
    """Форматоване виведення списку студентів з усіма 4 полями."""
    print("-" * 80)
    for item in listForPrinting:
        item_str = (
            f"Name = {item['name']:<10} | "
            f"Phone = {item['phone']:<12} | "
            f"Email = {item['email']:<18} | "
            f"Group = {item['group']}"
        )
        print(item_str)
    print("-" * 80)


def findPosition(listForFinding, nameForFinding):
    """Пошук позиції для збереження списку відсортованим за алфавітом."""
    index = 0
    for item in listForFinding:
        if item["name"].lower() < nameForFinding.lower():
            index += 1
        else:
            break
    return index


def addElemToSortedList(listForAdd, newElem):
    """Вставка нового елемента на знайдену позицію."""
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)


def getElement():
    """Зчитування всіх 4-х атрибутів студента з консолі."""
    name = input("Please enter the name: ").strip()
    phone = input("Please enter the phone: ").strip()
    email = input("Please enter the email: ").strip()
    group = input("Please enter the group: ").strip()
    return {"name": name, "phone": phone, "email": email, "group": group}


def deleteElem(listForDel, name):
    """Видалення студента за введеним ім'ям."""
    for idx, item in enumerate(listForDel):
        if item["name"].lower() == name.lower():
            del listForDel[idx]
            return True
    return False


def updateElement(listForUpdate):
    """Оновлення інформації про студента зі збереженням алфавітного порядку."""
    name = input("Please enter the name of the student to update: ").strip()
    target_idx = None

    for idx, item in enumerate(listForUpdate):
        if item["name"].lower() == name.lower():
            target_idx = idx
            break

    if target_idx is not None:
        old_elem = listForUpdate.pop(target_idx)
        print(f"Updating data for {name} (leave empty to keep current value):")

        new_name = input(f"Enter new name [{old_elem['name']}]: ").strip()
        new_phone = input(f"Enter new phone [{old_elem['phone']}]: ").strip()
        new_email = input(f"Enter new email [{old_elem['email']}]: ").strip()
        new_group = input(f"Enter new group [{old_elem['group']}]: ").strip()

        updated_elem = {
            "name": new_name if new_name else old_elem["name"],
            "phone": new_phone if new_phone else old_elem["phone"],
            "email": new_email if new_email else old_elem["email"],
            "group": new_group if new_group else old_elem["group"],
        }

        addElemToSortedList(listForUpdate, updated_elem)
        print("Element has been successfully updated")
    else:
        print("Element hasn't been found")


def main():
    while True:
        choice = input("\nPlease specify the action [C create, U update, D delete, P print, X exit]: ").strip()

        match choice:
            case "C" | "c":
                new_elem = getElement()
                addElemToSortedList(globalList, new_elem)
                print("New element has been added")
            case "U" | "u":
                updateElement(globalList)
            case "D" | "d":
                name_for_del = input("Please enter the name for delete: ").strip()
                if deleteElem(globalList, name_for_del):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p":
                printAllList(globalList)
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong operation")


if __name__ == "__main__":
    main()