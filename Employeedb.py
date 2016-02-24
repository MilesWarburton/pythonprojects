class Employeedb:
    def __init__(self):
        self.employeedict = {}




    def addemployee(self, name, salary):
        self.employeedict[name] = salary
        print(self.employeedict)





newEmployee = Employeedb()
newEmployee.addemployee("Mark", 300)
newEmployee.addemployee("Richard", 300)
newEmployee.addemployee("Sheldon", 9000)

