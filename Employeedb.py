import csv

class Employeedb:
    def __init__(self):
        self.employeedict = {}


    def addemployee(self, name, salary, occupation):
        self.employeedict[name] = float(salary)
        with open('employeedb.csv', 'a') as csvfile:
            fieldnames = ['first_name', 'salary', 'occupation']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            csvfilecount = csvfile.tell()
            if csvfilecount == 0:
                writer.writeheader()
                writer.writerow({'first_name': name, 'salary': float(salary), 'occupation': occupation})
            else:
                writer.writerow({'first_name': name, 'salary': float(salary), 'occupation': occupation})
            




    def avgsalary(self):
        salaries = []
        for key, val in self.employeedict.items():
            salaries.append(val)
        avg = sum(salaries)/len(salaries)
        return avg









