#David Piro
#6/6/2022
#Module 5 Assignments - In Class

"""
ArtShow.py - This program determines if an art show attendee gets a
                5% discount for preregistering.
Input: Interactive.
Output: A statement telling the user if they get a discount or no discount.
"""

# Write discount function here.
def discount():
    print("You are preregistered and qualify for a 5% discount.")

# Write noDiscount function here.
def noDiscount():
    print("Sorry, you did not preregister and do not qualify for a 5% discount.")

#User Input
registerString = input("Did you preregister? Enter Y or N: ")

# Test input here. If Y, call discount(), else call noDiscount().
if (registerString.upper() == 'Y'):
    discount()
elif (registerString.upper() == 'N'):
    noDiscount()
else:
    print("Thank you for participating.")

