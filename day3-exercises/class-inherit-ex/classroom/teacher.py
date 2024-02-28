from .person import Person

class Teacher(Person):
    def __init__(self, name, lastname, course):
        Person.__init__(self, name, lastname, "Teacher")
        self.course = course

    def get_name_and_course(self):
        return self.name + ' ' + self.lastname + ': ' + self.course
    

