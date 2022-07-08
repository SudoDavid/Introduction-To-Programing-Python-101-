#David Piro
#7/8/2022
#Module 7 In Class Program

#using the for loop:
#Write a loop that will let a user enter as many numbers as they wish. 
def userentry():
    user = 'Y'
    listitem = 0
    numberlist = []
    while user.upper() == 'Y':
        listitem = int(input("Please enter a number. \n"))
        numberlist.append(listitem)
        user = str(input("Would you like to enter another number? Y or N \n"))
    return numberlist
#Write a function to add all the negative numbers in the list and return the result
def findnegative(completedlist):
    total = 0
    for x in completedlist:
        if x < 0:
            total = total + x
    return total
#Write a function that will add all the positive numbers in the list and return the result
def findpositive(completedlist):
    total = 0
    for x in completedlist:
        if x > 0:
            total = total + x
    return total
#Write a function that will add all of the numbers in the list and return the result
def totals(completedlist):
    total = 0
    for x in completedlist:
        total = total + x
    return total

#main function definition
def main():
    #call method to write list
    completedlist = userentry()

    #Call the three functions
    #find the negatives
    negativelist = findnegative(completedlist)
    #find the positives
    positivelist = findpositive(completedlist)
    #find total sum
    finallist = totals(completedlist)

    #Print the results
    print(negativelist)
    print(positivelist)
    print(finallist)
    
    #Print the list 
    print(completedlist)

#main function call
main()