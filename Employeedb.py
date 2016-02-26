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









