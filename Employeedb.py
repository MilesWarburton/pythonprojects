class Employeedb:
    def __init__(self):
        self.employeedict = {}




    def addemployee(self, name, salary):
        self.employeedict[name] = float(salary)


    def avgsalary(self):
        salaries = []
        for key, val in self.employeedict.items():
            salaries.append(val)
        avg = sum(salaries)/len(salaries)
        print(avg)










newEmployee = Employeedb()
newEmployee.addemployee("Mark", 300)
newEmployee.addemployee("Richard", 300)
newEmployee.addemployee("Sheldon", 9000)
newEmployee.avgsalary()

