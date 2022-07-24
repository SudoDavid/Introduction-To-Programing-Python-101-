#Professor Piro
#7/24/2022

#Import Statements
import os

#Initalize variables
ScoresArray = []

#Create a textfile called Scores.txt
def CreateFile():    
    f = open("Scores.txt", "x")
    return f
#Write a program to input scores for a class.
def InputScores():
    x = 0
    Boolean = True
    while (Boolean):
        x = int(input("Please enter a test score. \n"))
        ScoresArray.append(x)
        nextEntry = input("Would you like to enter another test score? Y for continue, N to Stop \n")
        if nextEntry.upper() == 'Y':
            Boolean = True
        else:
            Boolean = False
            return ScoresArray 
#Write the grades to Scores.txt
def SaveScores(f, ScoresInput):
    f = open("Scores.txt", "w")
    with open('Scores.txt', 'w') as file:
        f.write('\n'.join(str(year) for year in ScoresInput))
    f.close()
#Open the file and read the scores and calculate the average.
def ReadScores():
    f = open("Scores.txt", "r")
    print(f.read())
    f.close()

###################
#Main Method
def main():
    os.remove("Scores.txt")
    f = CreateFile()
    ScoresInput = InputScores()
    SaveScores(f, ScoresInput)
    ReadScores()

#Program Start
main()









####################################
#OPTIONAL:
#Create a file with name, score
#Use CSV to read the file
#Print each name and score and print the averge.