#David Piro
#Last Updated 7/26/2022
#Created 7/26/2022
#######################

#Open the class file named Rectangle.py
#In the Rectangle class, create two attributes named length and width.
#Write a public calculateArea method and a public calculatePerimeter method to calculate and return the area of the rectangle and the perimeter of the rectangle.
from turtle import width
class Rectangle(object):
    # Declare public methods here
    def __init__(self, length, width):
        # Set class instance variables here
        self.length = length
        self.width = width

    def calculateArea(self):
        # Write calculateArea here
        area = (self.length) * (self.width)
        print(area)
        return area

    def calculatePerimeter(self):
        # Write calculatePerimeter here
        perimeter = ((self.length) * 2 )+((self.width) * 2)
        print(perimeter)
        return perimeter

r1 = Rectangle(3,4)
r1.calculateArea()

r2 = Rectangle(10,5)
r3 = Rectangle(7,3)
#Part2
r2.calculatePerimeter()
r2.calculateArea()
r3.calculateArea()
r3.calculatePerimeter()
