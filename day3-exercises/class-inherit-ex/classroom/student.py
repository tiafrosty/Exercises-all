from .person import Person

class Student(Person):
    def __init__(self, name, lastname, subject_area):
        Person.__init__(self, name, lastname, "Student")
        self.subject_area = subject_area

    def get_name_and_subject(self):
        return self.name + ' ' + self.lastname + ': ' +  self.subject_area 

