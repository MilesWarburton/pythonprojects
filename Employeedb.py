class Employeedb:
    def __init__(self):
        self.employeedict = {}




    def addemployee(self, name, salary):
        self.employeedict[name] = salary
        print(self.employeedict)





newEmployee = Employeedb()
newEmployee.addemployee("Mark", 300)
newEmployee.addemployee("Daniel", 300)
newEmployee.addemployee("Ben", 9000)

