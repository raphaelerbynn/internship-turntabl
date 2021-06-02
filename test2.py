class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def speak(self):
        print("'Hello, I'm", self.name)

    def walk(self):
        print("Walking away")

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(2021 - self.date_of_birth)


mary = Person("Mary", 1999)
mary.get_age()
