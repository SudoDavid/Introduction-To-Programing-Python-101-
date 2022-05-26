def housekeeping(): 
    #Print the names of the people in the group 
    group = input("Please enter the name of people in your group \n")
    return group

def getName(): 
    name = input("Please your name \n")
    print(name)
    return name
    
def getMajor(): 
    major = input("Please enter the major \n")
    print(major)
    return major

#use elif to determine the advisor  
def findAdvisor(major): 
    # Computer Science is Albert Nault 
    if (major == 'Computers'):
        print("Albert Nault")
    # AA is Stephanie Smith 
    elif (major == 'AA'):
        print("Steph Smith")
    # Athletics is Melissa Miller 
    elif (major == 'Athletics'):
        print("Melissa Miller ")
    # Nursing is Sarah Gingrich 
    elif (major == 'Nursing'):
        print("Sarah Gingrich")
      # Health Professions is Cassie Steves 
    elif (major == 'Health'):
        print("Cassie Steves")  
    else:
        print("No advisor assigned")
     
def calcGrade(): 
    #input grade 
    grade = int(input("Please enter a grade as a number. \n"))Y
    #Use either in range and elif to determine the grade OR use AND stmts and elif 
    if (grade >= 90) and (grade <= 100):
        print("A")
    elif (grade >= 80) and (grade <= 89):
        print("B")
    elif (grade >= 70) and (grade <= 79):
        print("C")
    elif (grade >= 60) and (grade <= 69):
        print("D")
    else:
        print("F")
    #print the grade 

###################################
#This is main 
def main():
    #Create a loop to keep getting data until user wants to stop 
    x = input("Please enter Y to continue, otherwise stop \n")
    while (x.upper() == 'Y'):
        housekeeping() 
        name = getName() 
        major = getMajor() 
        findAdvisor(major) 
        calcGrade() 
        x = input("Please enter Y to continue, otherwise stop \n")

# Main Function Call
main()