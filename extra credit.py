#import statement for sys.exit()
import sys
#list for days and months
month = ['January', 'February', 'March ', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = ['31', '28', '31', '30', '31' '30', '31', '31', '30', '31', '30', '31']
#user input
months = input('Please enter a month in full spelling, example: January \n')
days = input('Please enter a day of the month, example: 30 \n')
#verify if month is within the list
x = 0
#compare input to each list entry for month
while x < len(month):
    # Compare if month is within list
    if month[x] == months:
        #while days input is less than the max day in the list
        while days <= max(day):
            #if list is greater than or equal to days
            if day[x] >= days:
                #print and exit
                print('Input is Valid')
                sys.exit()
            #increment list
            x += 1    
    else:
        #increment list
        x += 1
print('Not Valid')
#end