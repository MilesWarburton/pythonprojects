from Employeedb import Employeedb

newEmployee = Employeedb()

    while True:
        inputName = input("Employee Name: ")
        inputSalary = float(input("Employee Salary: "))
        newEmployee.addemployee(inputName, inputSalary)
        print(newEmployee.avgsalary())
        answer = input("Would you like to continue? Yes or No")
        if answer == "yes":
            pass
        if answer ==" ":
            print("Please type Yes or No")
        elif answer == "no":
            print("Bye!")
            break
