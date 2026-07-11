class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetails()

eng1 = Engineer("NS", 20)
print(eng1.name)
eng1.showDetails()
