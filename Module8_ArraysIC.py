deptSalary= [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

departName = ["Personnel", "Marketing", "Manufacturing", "Computer Services", "Sales", "Accounting", "Shipping"]


#Method Declarations
def printDeptList():
    print("1 - Personnel")
    print("2 - Marketing")
    print("3 - Manufacturing")
    print("4 - Computer Services")
    print("5 - Sales")
    print("6 - Accounting")
    print("7 - Shipping")

#Method to take user input for valdiating department   
def validateDept(department):
    if department == 1:
        print("You have selected:", department)
        return department
    elif department == 2:
        print("You have selected:", department)
        return department
    elif department == 3:
        print("You have selected:", department)
        return department
    elif department == 4:
        print("You have selected:", department)
        return department
    elif department == 5:
        print("You have selected:", department)
        return department
    elif department == 6:
        print("You have selected:", department)
        return department
    elif department == 7:
        print("You have selected:", department)
        return department
    else:
        print("Error: You have an invalid selection:", department)
        return department
        
def validateHours():
    x = int(input("Please enter the number of hours worked for the day. \n"))
    #Use of Try Except
    try:
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")
    #Try Raise TypeError
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
    return x
def validateRate():
    z = int(input("Please enter the hourly rate of pay. \n"))
    #Use of Try Except
    try:
        print(z)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")
    #Try Raise TypeError
    if not type(z) is int:
        raise TypeError("Only integers are allowed")
    return z

def deptWages(d,h,hr):
    emptotal = h*hr
    dailytotal = deptSalary[(d-1)] + emptotal
    if d == 1:
        deptSalary[0] = dailytotal
    elif d == 2:
        deptSalary[1] = dailytotal
    elif d == 3:
        deptSalary[2] = dailytotal
    elif d == 4:
        deptSalary[3] = dailytotal
    elif d == 5:
        deptSalary[4] = dailytotal
    elif d == 6:
        deptSalary[5] = dailytotal
    elif d == 7:
        deptSalary[6] = dailytotal
    else:
        print("Error: Something went wrong.")
def printTotalSalary():
    print("Department 1:")
    print(departName[0])
    print(deptSalary[0])
    print("-----------")
    print("Department 2:")
    print(departName[1])
    print(deptSalary[1])
    print("-----------")
    print("Department 5:")
    print(departName[2])
    print(deptSalary[2])
    print("-----------")
    print("Department 4:")
    print(departName[3])
    print(deptSalary[3])
    print("-----------")
    print("Department 5:")
    print(departName[4])
    print(deptSalary[4])
    print("-----------")
    print("Department 6:")
    print(departName[5])
    print(deptSalary[5])
    print("-----------")
    print("Department 7:")
    print(departName[6])
    print(deptSalary[6])
    print("-----------")

#program start
def main():
    again = "Y"
    dept = 0
    while again.upper() == "Y":
        print("You will need to enter the employee's department number, hours worked and hourly salary")
        printDeptList()
        #Get valid input for dept. number, hours worked, and hourly salary
        department = int(input("Please enter a #1-7 for your employee department number."))
        dept = validateDept(department)
        #validate hours
        hours = validateHours()
        #Find HourlyRate
        hourlyrate = validateRate()
        #add to correct department list  
        deptWages(dept,hours,hourlyrate)
        #continue?
        again = input("Enter Y to continue: \n")
    #printTotalSalary
    printTotalSalary()
    #end main
main()