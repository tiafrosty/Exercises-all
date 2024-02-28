from classroom import Teacher, Student

# Create an object of a class student
new_student = Student('Taya', 'Morozova', 'Math')
print(new_student.get_name_and_subject())
# And teacher
new_teacher = Teacher('Filipe', 'Maia', 'programming with Python')
print(new_teacher.get_name_and_course())