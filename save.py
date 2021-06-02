
class ContactDetails():

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def add(self, name, contact):
        contact.update({self.name: self.number})

    def get_contacts(self):
        print(self.contacts)

    def delete(self):
        pass

    def list_contact(self):
        pass

    def update_contact(self):
        pass


contact = save_contact('ama', 9)
contact.add('kweku', {3:3})
contact.get_contacts()