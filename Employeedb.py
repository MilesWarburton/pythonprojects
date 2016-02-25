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
        return avg

#newemployee = Employeedb()
#newemployee.addemployee("Rache", 45000)
#newemployee.addemployee("Vicky", 56778)
#newemployee.addemployee("Mark", 300)
#newemployee.addemployee("Richard", 300)
#newemployee.addemployee("Sheldon", 9000)
#print(newemployee.avgsalary())










