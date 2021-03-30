from classes import Person, Employee

person2 = Person('Katy', 32)
person2.age = 40
person2.print_info()

employee = Employee('Nik', 22, 'Google')
employee.print_info()
employee.more_info()
print(employee)
