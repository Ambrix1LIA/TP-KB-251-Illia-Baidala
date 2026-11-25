class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return self.name + " | " + self.phone + " | " + self.email + " | " + self.group