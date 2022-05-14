#David Piro 
#COP1000 – Program 1
#5/14/2022 – Version 1.0
###########################################
###########################################
#Import Statements
import string


#Example 1: Input
entry = input("Please enter a number \n")

#Example 2: Output of the input
print("The user has entered:", entry)
    
#Example 3: Different Types of Variables
#bool
#int 
#float
#complex 
#string

#Example 4: Constants
GRAVITY = 9.8
#Example 5: Arithmetic Operators
x = 6
y = 2
z = 0
#Add
z = x + y
#Subtract
z = x - y
#Multiply
z = x * y
#Divide
z = x / y
#Modulus
z = x % y
#Exponential
z = x ** y
#Floor Division
z = x // y

#Example 6: If-else 
if y > x:
  print("x is greater than y")
elif y == x:
  print("y and x are equal")
else:
  print("y is greater than x")  

#Example 7: Problem
# Create your variables here
myCurrentAge = 31
currentYear = 2022

#Execute Statements
myNewAge = myCurrentAge + (2050 - currentYear)
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")

#Example 8: Summary Problem
itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Write your assignment statements here for profit, salePrice, and saleProfit
profit = retailPrice - wholesalePrice
salePrice = retailPrice*.75
saleProfit = salePrice - wholesalePrice

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))

