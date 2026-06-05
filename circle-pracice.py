class Employee():
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role:",self.role)
        print("department:",self.department)
        print("salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.nae = name
        self.age = age
        super().__init__("engineer","development",40000)





e1 = Engineer("ajju",1000)
e1.showDetails()