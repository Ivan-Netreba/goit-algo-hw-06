from collections import UserDict

# Базовий клас для полів запису.
class Field():
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    def __init__(self, value: str):
        if value:
            super().__init__(value)
        else:
            raise ValueError
              
# Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
class Phone(Field):
    def __init__(self, value: str):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError
        
	
 # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name: Name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        for  phone in self.phones:
            if phone.value == number:
               self.phones.remove(phone)
            else:
                raise ValueError

    def edit_phone(self, old_number: str, new_number: str):
        if new_number.isdigit() and len(new_number) == 10:
            for phone in self.phones:
                if phone.value == old_number:
                    phone.value = new_number
                    break
        else:
            raise ValueError

    def find_phone(self, number: str) -> Phone:
        for phone in self.phones:
            if phone.value == number:
                return phone

    def __str__(self):
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання та управління записами.
class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
 


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
