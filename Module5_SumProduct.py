#David Piro
#6/6/2022
#Module 5 Assignments - In Class Part 2

# Write sums() function here.
def sums(number):
    numbers = number + number
    print(numbers)

# Write products() function here.
def products(number):
    number = number * number
    print(number)

numberString = input("Enter a positive integer or 0 to quit: ")
number = int(numberString)

while number != 0:
    # Call sums() function here.
    sums(number)
    # Call products() function here.
    products(number)
    numberString = input("Enter a positive integer or 0 to quit: ")
    number = int(numberString)
