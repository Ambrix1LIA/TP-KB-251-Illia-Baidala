import lab_02

def test_add_student():
    lab_02.students = []
    lab_02.add_student("Bob", "111", "b@mail.com", "KB-251")
    lab_02.add_student("Alice", "222", "a@mail.com", "KB-251")
    assert len(lab_02.students) == 2
    assert lab_02.students[0]["name"] == "Alice"
    assert lab_02.students[1]["name"] == "Bob"

def test_delete_student():
    lab_02.students = [{"name": "Bob", "phone": "111", "email": "b@mail.com", "group": "KB-251"}]
    assert lab_02.delete_student("Bob") == True
    assert len(lab_02.students) == 0
    assert lab_02.delete_student("NonExistent") == False

def test_update_student():
    lab_02.students = [{"name": "Bob", "phone": "111", "email": "b@mail.com", "group": "KB-251"}]
    lab_02.update_student("Bob", "Zak", "999", "z@mail.com", "KB-252")
    assert lab_02.students[0]["name"] == "Zak"
    assert lab_02.students[0]["phone"] == "999"

def test_save_and_load(tmp_path):
    test_file = tmp_path / "test.csv"
    lab_02.students = [{"name": "Alice", "phone": "123", "email": "a@mail.com", "group": "KB-251"}]
    lab_02.save_data(str(test_file))
    lab_02.load_data(str(test_file))
    assert len(lab_02.students) == 1
    assert lab_02.students[0]["name"] == "Alice"