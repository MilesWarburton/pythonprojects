class Employeedb:
    def __init__(self):
        self.employeedict = {}




    def addemployee(self, name, salary):
        self.employeedict.update({'Name': name, 'Salary': salary})
        print(self.employeedict.values())





newemployee = Employeedb()
newemployee1 = Employeedb()
newemployee2 = Employeedb()

newemployee.addemployee('Spoodman', 20000)
newemployee1.addemployee('Spoodman', 20000)
newemployee2.addemployee('Spoodman', 20000)