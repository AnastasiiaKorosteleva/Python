__author__ = 'anastasiiakorosteleva'

class BioInfSchool:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Новый участник: {0})".format(self.name))
    def information(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Member(BioInfSchool):
    def __init__(self, name, age, courses, position):
        BioInfSchool.__init__(self, name, age)
        self.courses = courses
        self.position = position
        print('(Новый сотрудник: {0})'.format(self.name))
    def information(self):
        BioInfSchool.information(self)
        print('Преподаваемые курсы: "{0}" Должность: "{1}" '.format(self.courses, self.position), end=" ")

class Student(BioInfSchool):
    def __init__(self, name, age, marks, projects, attendance ):
        BioInfSchool.__init__(self, name, age)
        self.marks = marks
        self.projects = projects
        self.attendance = attendance
        print('(Новый студент: {0})'.format(self.name))
    def information(self):
        BioInfSchool.information(self)
        print('Рейтинг: "{0}" Участие в проектах: "{1}" Посещаемость: "{2}" '.format(self.marks,
                                                                                          self.projects,
                                                                                          self.attendance), end=" ")



first = Member('Konstantin Zaytsev', 22, "Python for biologists", "Teacher")
second = Student('Vasya Pupkin', 19, "75%", "study of NGS", "100%")

print()

members = [first, second]
for member in members:
    member.information()

# Student("Kozinak", 29, "75%", "study of protein-protein interaction", "50%").information()