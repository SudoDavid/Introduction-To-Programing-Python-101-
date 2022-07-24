#Professor Piro
#7/24/2022

#a. Professor Zak allows students to drop the four lowest scores on the ten 100-point quizzes she gives during the semester. 
# Design an application that accepts a student name and 10 quiz scores. 
# Output the student's name and total points for the student's six highest-scoring quizzes.

#initiliaze variables
from tokenize import Name

QuizScores = []
newQuizScores = []

#Accept Name
def getName():
    name = input("Please enter the name of the student \n")
    print("Hello " + name)
    return name

#Accept Quiz Scores
def getQuizzes(QuizScores):
    x = 0
    y = 0
    Boolean = True
    while (Boolean):
        x = int(input("Please enter a test score. \n"))
        QuizScores.append(x)
        y = y + 1
        if  y == 10:
            Boolean = False
            return QuizScores 
        else:
            Boolean = True
#SortQuizzes
def sortQuizzes(Quizscores):
    bubblesort(Quizscores)
    return QuizScores

#Sorting Algorithm
def bubblesort(QuizScores):
    n = len(QuizScores)
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if QuizScores[j] > QuizScores[j + 1]:
                swapped = True
                QuizScores[j], QuizScores[j + 1] = QuizScores[j + 1], QuizScores[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return QuizScores
#DropQuizzes
def dropQuizzes(QuizScores):
    z = 0
    while z !=4: 
        QuizScores.pop(z)
        z = z + 1
    return QuizScores

def findTotal(newQuizScores):
    n = len(newQuizScores)
    z = 0
    while z != 6:
        newQuizScores[0] = newQuizScores[0] + newQuizScores[z]
        z = z + 1
    return newQuizScores  
#Main Method Definition
def main():
    print("Get Ready to Enter Student Name and Quiz Scores \n")
    studentName = getName()
    getQuizzes(QuizScores)
    sortQuizzes(QuizScores)
    newQuizScores = dropQuizzes(QuizScores)
    findTotal(newQuizScores)

    print('##########')
    print(studentName)
    print(newQuizScores[0])

#Main Method Call
main()