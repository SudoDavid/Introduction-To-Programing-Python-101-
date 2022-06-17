#David Piro
#6/16/2022
#Module 6
#You are going to create a program that calculates prices for custom made house signs.

def housekeeping():
    sign_wording = str(input("Please enter the 'lettering' for your sign, with maximum of 8 characters \n"))
    if len(sign_wording) > 8:
        print("Please use less than 8 characters \n")
        sign_wording = str(input("Please enter the 'lettering' for your sign, with maximum of 8 characters \n"))
        return sign_wording
    else:
        return sign_wording

def wood():
    wood_type= int(input("Please select wood type: 1 for 0ak, 2 for Elk, and 3 for Pine \n"))
    if (wood_type == 1):
        return 'Oak'
    elif (wood_type == 2):
        return 'Elk'
    else: 
         return 'Pine'
        
def CalcChar(sign_lettering):
    char_length = len(sign_lettering)
    char_cost = char_length * 20.00
    return char_cost

def CalcColors():
    color= int(input("Per character: Would you like Gold lettering $8? or Silver for $9? Press 1 for Gold, 2 For Silver \n"))
    if (color == 1):
        return 'Gold'
    elif (color == 2):
        return 'Silver'
    else: 
         return 'Gold'

def CalcCost(base_cost, color_type):
    num_letters = base_cost / 20
    if (color_type == 'Gold'):
        cost = num_letters * 8
        final_cost = cost + base_cost
        return final_cost
    else:
        cost = num_letters * 9
        final_cost = cost + base_cost
        return final_cost

def main():
    #accept user input for sign
    sign_lettering = housekeeping()
    #Determine material type
    wood_selection = wood()
    #Calculate Charcter Cost
    base_cost = CalcChar(sign_lettering)
    #Calculate color cost
    color_type = CalcColors()
    #total cost
    total_cost = CalcCost(base_cost, color_type)
    #print total cost
    print(total_cost)
main()