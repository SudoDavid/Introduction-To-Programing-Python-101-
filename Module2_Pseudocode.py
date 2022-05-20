#OYO Flowchart converted to Python
#Includes pseudo code comments
#Professor Piro
#5/18/2022

#Prompt the user to enter a sales tax rate.
#Variable declared with float to convert data type from string to float for decimal inputs
#input function from python library called to accept user input
print("I'm going to calculate the total price for you!")
sales_tax = float(input("Please enter a sales tax rate in decimal form \n"))

#Prompt the user to enter a price.
product_price = float(input("Please enter the product price, include decimals. \n"))

#Calculate and output the amount of tax for the item and the total price with tax.
#total tax 
total_tax = product_price*sales_tax
print()
print("The total tax is: \n")
print(total_tax)

#total price
print()
print("The total price is: \n")
total_price = product_price + total_tax
print(total_price)