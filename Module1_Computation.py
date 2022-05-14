
#IF the number is > 10 – Say “You Win xxxx”
#if the number is <=10 – Say “You Lose xxxx”

name = input("What is your name? \n")
number = int(input("What is your number? \n"))

print("Hello: ", name)
if(number > 10):
    print("You Win:", name)
elif(number <= 10):
    print("You lose:", name)
else:
    print("Something went wrong")


#Tax Calculation
#housekeeping
salary = 1250.00
numDependents = 2
stateTax = 0
federalTax = 0
dependentDeduction= 0
totalWithholding = 0

#Process and Output
# Calculate stateTax here.
stateTax = salary * .065
print("State Tax: $" + str(stateTax))

# Calculate federalTax here.
federalTax= salary * .28
print("Federal Tax: $" + str(federalTax))

# Calculate dependantDeduction here.
dependentDeduction = (float(salary) * .025)*int(numDependents)
print("Dependents: $" + str(dependentDeduction))

# Calculate totalWithholding here.
totalWithholding = float(stateTax) + float(federalTax) + float(dependentDeduction)

# Calculate takeHomePay here.
takeHomePay = float(salary) - float(totalWithholding)
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))