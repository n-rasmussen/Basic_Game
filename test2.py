
class Test():
    def __init__(self, name):
        self.name = name


class Teacher(Test):
    def __init__(self, subject):
        super(Teacher, self).__init__(subject)
        self.subject = subject
        self.speed = 20


person = Teacher("French")
person.name = "bob"

print(person.name)
print(person.subject)
print(person.speed)