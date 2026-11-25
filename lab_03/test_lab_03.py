from student import Student
from student_list import StudentList
from utils import Utils

def test_student_init():
    s = Student("Bob", "111", "b@mail.com", "KB-251")
    assert s.name == "Bob"
    assert str(s) == "Bob | 111 | b@mail.com | KB-251"

def test_add_and_sort():
    sl = StudentList()
    sl.add_student(Student("Bob", "111", "b@mail.com", "KB-251"))
    sl.add_student(Student("Alice", "222", "a@mail.com", "KB-251"))
    assert len(sl.students) == 2
    assert sl.students[0].name == "Alice"
    assert sl.students[1].name == "Bob"

def test_delete():
    sl = StudentList()
    sl.add_student(Student("Bob", "111", "b@mail.com", "KB-251"))
    assert sl.delete_student("Bob") == True
    assert len(sl.students) == 0
    assert sl.delete_student("Zak") == False

def test_update():
    sl = StudentList()
    sl.add_student(Student("Bob", "111", "b@mail.com", "KB-251"))
    sl.update_student("Bob", "Zak", "999", "z@mail.com", "KB-252")
    assert sl.students[0].name == "Zak"
    assert sl.students[0].phone == "999"

def test_file_io(tmp_path):
    test_file = tmp_path / "test.csv"
    utils = Utils(str(test_file))
    sample = [Student("Bob", "111", "b@mail.com", "KB-251")]
    utils.save_data(sample)
    loaded = utils.load_data()
    assert len(loaded) == 1
    assert loaded[0].name == "Bob"