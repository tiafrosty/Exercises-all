class Person:
    def __init__(self, name, lastname, role):
        self.name = name
        self.lastname = lastname
        self.role = role

    def get_name_and_lastname(self):
        return self.name + ' ' + self.lastname 

    def __str__(self):
        return "The person full name is %s %s" % (self.name, self.lastname)