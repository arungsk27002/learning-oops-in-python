class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print("role :",self.role)
        print("department :",self.department)
        print("salary :",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","200000")
eng1=Engineer("arun",21)
print(eng1.department)