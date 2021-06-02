
class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def speak(self):
        print("Hello, I'm", self.name)

    def walk(self):
        print("Walking away")

    def get_name(self):
        print(self.name)

    def get_age(self):
        return 2021 - self.date_of_birth


class Student(Person):
    def __init__(self, name, date_of_birth, course_names):
        super().__init__(name, date_of_birth)
        self.course_names = course_names

    def get_courses(self):
        return self.course_names


class Worker(Person):
    def __init__(self, name, date_of_birth, work_place):
        super().__init__(name, date_of_birth)
        self.work_place = work_place

    def get_workplace(self):
        return self.work_place


courses_john = ['Maths', 'Chinese']
courses_ralph = ['CS', 'Acc']

john = Student('John', 1999, courses_john)
ralph = Student('Ralph', 1999, courses_ralph)

emma = Person('Emma', 2001)

print(*john.get_courses(), sep=', ')
print(john.get_age(), sep=', ')

print(*ralph.get_courses())







