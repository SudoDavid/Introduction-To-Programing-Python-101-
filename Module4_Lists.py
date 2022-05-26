# David Piro
# 5/25/2022
# Example 1 Looping through a list
##############################################
#squares = [1, 4, 9, 16]
#sum = 0
#for num in squares:
#   sum += num
#print(sum)


#List Example
# Empty List 
fruits = []
#Print List
print(fruits)
#List of 5 Index and 6 Elements
fruits = ['Apples,', 'Oranges', 'Grapes', 'Strawberries', 'Pineapple', 'Mango']
print(fruits)

#List Examples Continued
#Append
fruits.append('Peach')
print(fruits)

#Insert
fruits.insert(3,'Pear')
print(fruits)

# index search and print
print(fruits.index('Grapes'))

#Remove
fruits.remove('Pineapple')
print(fruits)

#Sort and print
print(fruits.sort())

#reverse
fruits.reverse()
print(fruits)

#Pop, find the index and pop Grapes
print(fruits.index('Grapes'))
fruits.pop(5)
print(fruits)