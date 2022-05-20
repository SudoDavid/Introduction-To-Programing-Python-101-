#A. Write the code snippets that do the following:
#Assign the value 20 to the variable y and assign the value 40 to the variable z if the variable x is greater than 100.
x = int(input("Please enter a value for x"))
if  x > 100:
    y = 20
    z = 40
    print("x is 20 and y is 40")
else:
    print("X is less than 100")

#Assign the value 0 to the variable b and assign the value 1 to the variable c if the variable a is less than 10.
a = int(input("Please enter a value for a"))
if a < 10:
    b = 0
    c = 1
    print("a is less than 10")
else:
    print("a is greater than 10")

#Display "Speed is Normal" if the variable speed is between 55 and 70.  Otherwise, display "Not Going the Speed Limit"
x = int(input("What is your speed?"))
if x > 55 and x < 70:
    print("Speed is normal")
else:
    print("Not going the speed limit")

#If amount1 is greater than 10 and amount2 is less than 100, display the greater one.
amount1= int(input("Please enter a value"))
amount2 = int(input("Please enter another value"))
if amount1 > 10 and amount2 < 100:
    if amount1 < amount2:
        print(amount2)
    elif amount2 < amount1:
        print(amount1)
    else:
        print("Error")
else:
    print("End Program")

