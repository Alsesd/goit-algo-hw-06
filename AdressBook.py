from collections import UserDict

class Field:
    def __init__(self, value, required=True):
        if required and not value:
            raise ValueError("This field is required")
        self.value = value

    
    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
    


class Phone(Field):
   def __init__(self, value, required=False):
        super().__init__(value)
        if not len(value) == 10:
            raise ValueError("Phone number must be 10 digits long")


class Record: #add phone, delete phone, change phone, search phone
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
            else:
                raise ValueError
            
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    pass
        


class AddressBook(UserDict): #add record, delete record, search record
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        result = ""
        for record in self.data.values():
            result += str(record) + "\n"
        return result.strip()


