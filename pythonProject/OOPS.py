class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary


harry = Employee("Harry", "8999")
print(harry.name)
print(harry.getSalary())

sarthak = Employee("Sarthak", "99999999")
print(sarthak.name)
print(sarthak.getSalary())