#David Piro
#6/6/2022
#Module 5 Assignments - In Class Part 5



#Write a program with two functions
def addToList(food):  
#Ask the user to input another food item.
    user_input = str(input("Please enter another food item \n"))
    food.append(user_input)

def printList(food): 
#Print the entire list
    print(food)
 
def removefromList(food):
    #Ask the user to remove another food item.
    user_input = str(input("Please remove another food item \n"))
    food.remove(user_input)

#The main program will create a list:  
myList = ["apple", "orange", "grapes"]

#Call the function printList, using myList
printList(myList)

#Call the function addToList, using myList
addToList(myList)

#Call the function printList, using myList
printList(myList)

#Add another function that asks the user for a food to remove.  Remove the food
#remove item
removefromList(myList)

#print list
printList(myList)