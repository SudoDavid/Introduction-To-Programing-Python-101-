#1.Write a program that will do the following:
#Prompt the user to enter their name.
user_name = input("Hi User, Please enter your name from birth. \n")
print(user_name)

#Print "Nice to meet you, XXX", where XXX is the name.
print("Nice to meet you,", user_name)

#2. Write a program that will do the following:
#Prompt the user to enter a sales tax rate
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

#3. Find Batting Average
hits = int(input("Enter the player's number of hits: \n"))

atBat = int(input("Enter the player's number of times the player was at bat: \n"))

battingAverage = float((hits/atBat))

print(battingAverage)