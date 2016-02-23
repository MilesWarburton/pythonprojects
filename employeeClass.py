class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def addemployee(self, name, salary):
        employeedict = ({})
        employeedict.update({'Name': name, 'Salary': salary})
        return employeedict

    def storeemployee(self, employeedict):
        storeemployee = []
        storeemployee.append(employeedict)
        for count, element in enumerate(storeemployee):
            print(count, element)
        return storeemployee

    def deleteemployee(self, storeemployee):
        del storeemployee[0]
        print(storeemployee)



newemployee = Employee("Miles", 2000)

newemployee.deleteemployee(newemployee.storeemployee(newemployee.addemployee(newemployee.name, newemployee.salary)))






