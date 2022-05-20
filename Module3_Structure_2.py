
#B. Write a program that determines if a student will be admitted or rejected.  
#Student will enter a test score and a class ranK.
test_score = int(input("Please enter a test score \n"))

class_rank = int(input("Please enter the class rank, ranging from 0 to 100 \n"))

#Conditions for Acceptance:  testScore >= 90   and classRank >=25
if test_score >= 90   and class_rank >=25:
    print("Student has been accepted!")

#Conditions for Acceptance: testScore >=80 and Class rank >=50
elif test_score >= 80   and class_rank >=50:
    print("Student has been accepted!")

#Everything else is Reject
else:
    print("Student has been rejected. :(")