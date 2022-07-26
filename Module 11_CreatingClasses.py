#David Piro
#Last Updated 7/26/2022
#Created 7/26/2022
#######################

#Problem 1
#Design a class named TermPaper that holds an author's name, the subject of the paper, 
#and an assigned letter grade. 
#Include methods to set the values for each data field and display the values for each data field. 
######
#Problem 1 Solution: Class Diagram
class TermPaper:
    def __init__(self, name, subject, grade):
       self.name = name
       self.subject = subject
       self.grade = grade

student1 = TermPaper("David", "Cybersecurity", "A-")

print(student1.name)
print(student1.subject)
print(student1.grade)

#Problem2
#Design a class named Computer that holds the make, model, and amount of memory of a computer. 
#Include methods to set the values for each data field, and include a method that displays all the values for each field. 
#Create the class diagram. You do not have to write the program that uses this class.
class Computer:
    def __init__(system, make, model, memory, storage, cpu):
       system.make = make
       system.model = model
       system.memory = memory
       system.storage = storage
       system.cpu = cpu

system1 = Computer("Dell", "Inspiron", "32GB", "2TB", "i9")

print(system1.make)
print(system1.model)
print(system1.memory)
print(system1.storage)
print(system1.cpu)