#User Enters Value Returns Result that was multiplied by 10
class problem1:
    x = int(input("Please enter a value \n"))
    y = x * 10
    print(y)

#Using variables with arithmetic operators
class problem2a:
    a = int(input("Please enter the number of hours worked in a day. \n"))
    b = a*5
    print(b)
#same problem  
class problem2b:
    e = int(input("Please enter the number of hours worked in a day. \n"))
    f = (e*252)
    print(f)

#Calculate area and perimeter of the rug
class problem3:
    length_of_rug = int(input("Please enter the length of the rug. \n"))
    width_of_rug = int(input("Please enbter the width of the rug. \n"))
    rug_perimeter = 2 * (length_of_rug + width_of_rug)
    print(width_of_rug)
    rug_area = (length_of_rug * width_of_rug)
    print(length_of_rug)

#method call for all problems and inputs
class main:
    problem1()
    problem2a()
    problem2b()
    problem3()
main()