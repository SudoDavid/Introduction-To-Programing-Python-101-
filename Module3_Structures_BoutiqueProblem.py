import datetime

#David Piro
#5/21/2022

#Main Method Defined
def main():
    student_info()
    print(get_ID())
    totalitems = get_salesitems()
    totalsales = get_salesamount()
    sales_status(totalitems, totalsales)

#CREATE A FUNCTION THAT WILL PRINT YOUR NAME, THE CLASS NAME AND THE DATE
def student_info():
    x = datetime.datetime.now()
    print("Hello, what is your name?")
    sales_person = input("My name is: ")
    print("Thank you,", sales_person)
    print("Introduction to Programming - Summer 2022")
    print(x)
################################
################################
################################
################################
#Write a program that accepts one salesperson's ID number, number of items sold in the last month, and total value of the items and displays data message only if the 
#salesperson is a high performer—defined as a person who sells more than 200 items in the month OR sells over $1,000 in the month.
#Cecilia's Boutique wants several lists of salesperson data.

#CREATE A FUNCTION THAT GETS THE ID AND RETURNS IT TO MAIN
#THE ID MUST BE NUMERIC (WHILE LOOP)
def get_ID():
    print("Hello, what is your ID number, (0-100)?")
    sales_ID = input("Identification #: ")
    return sales_ID

#CREATE A FUNCTION THAT GETS THE NUMBER OF ITEMS SOLD AND THE TOTAL SALES AMOUNT
#RETURNS BOTH TO MAIN
def get_salesitems():
    print("What were the total quantity  of items sold?")
    items_sold = int(input("")) 
    return items_sold

def get_salesamount():
    print("What were the total sales of items sold?")
    sales_total = int(input(""))
    return sales_total

#CREATE A FUNCTION THAT DETERMINES WHETHER THE SALESPERSON IS A HIGH SELLER
#PASS THE NUMBER OF ITEMS AND THE AMOUNT SOLD
def sales_status(totalitems, totalsales):
    if totalitems > 200:
        print("Congrads, you are a high seller!!!")
    elif totalsales > 1000:
        print("Congrads, you are a high seller!")
    else:
        print("You are not a high seller :(")

#Main Method Call
main()
