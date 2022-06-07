#David Piro
#6/6/2022
#Module 5 Assignments - In Class Part 4

# Calculator.py - This program performs arithmetic, ( +. -, *. / ) on two numbers.
# Input:  Interactive
# Output:  Result of arithmetic operation
result = 0

# Write performOperation function here
def performOperation(operation, numberOne, numberTwo):
    if(operation == '+'):
        result = numberOne + numberTwo
        return result
    elif(operation == '-'):
        result = numberOne - numberTwo
        return result
    elif(operation == '*'):
        result = numberOne * numberTwo
        return result
    elif(operation == '/'):
        result = numberOne / numberTwo
        return result
    else:
        print("Operator Error")

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
operation = input("Enter an operator (+ - * /): ")

# Call performOperation method here and store the value in "result"
result = performOperation(operation, numberOne, numberTwo)

print(str(numberOne) + " " + operation + " " + str(numberTwo) + " = " + str(result))
