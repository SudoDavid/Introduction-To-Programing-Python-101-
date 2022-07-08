#David Piro
#7/8/2022
#Module 7 In Class Program

#Write a program that accepts a last name and a reservation time.  Store the information in separate lists.

#The valid reservation times are:  6, 7, 8.
#Allow input until the user wants to stop.
#Print the following:
#Each diner along with their reservation time.
#The total number of diners who will be dining at 6, at 7, and at 8.
######################

#method for deleting reservation
#def deletereservation():


#Method for Reservation
def reservation():
    #initialize list
    sixoclock = []
    sevenoclock = []
    eightoclock = []

    name = ''
    time = 0
    totalreservations = 0

    sixtime = 0
    seventime = 0
    eighttime = 0
    #sequence variable
    continueinput = 'Y'

    while continueinput.upper() == "Y":
        time = str(input('Please enter a time to make a reservation at either, 6, 7, or 8. \n'))
        #If check for 6 O'Clock Reservation
        if time == '6' and sixtime <= 10:
            name = str(input('Please enter a name for the reservation. \n'))
            sixoclock.append(name)
            #reservation confirmation
            print("Reservation Completed for", name)
            totalreservations = 1 + totalreservations
            sixtime = 1 + sixtime
        #Elif check for 7 O'Clock Reservation
        elif time == '7' and seventime <= 10:
            name = str(input('Please enter a name for the reservation. \n'))
            sevenoclock.append(name)
            #reservation confirmation
            print("Reservation Completed for", name)
            totalreservations = 1 + totalreservations
            seventime = 1 + seventime
        #Elif check for 8 O'Clock Reservation
        elif time == '8' and eighttime <= 10:
            name = str(input('Please enter a name for the reservation. \n'))
            eightoclock.append(name)
            #reservation confirmation
            print("Reservation Completed for", name)
            totalreservations = 1 + totalreservations
            eighttime = 1 + eighttime
        else:
            print("Please enter a valid time. \n")
        #endwhile
        continueinput = input("Do you want to continue?, enter Y or N. \n")

    #Print totals for reservations and each time slot
    print("The reservations made at 6:00 PM were for", sixoclock)
    print("The reservations made at 7:00 PM were for", sevenoclock)
    print("The reservations made at 8:00 PM were for", eightoclock)
    print("The total number of reservations for the night is:", totalreservations)

    reservationlist = sixoclock + sevenoclock + eightoclock
    return reservationlist
#main method definition
def main():
    reservations = []
    reservations = reservation()
    print(reservations)
    #call removalmethod

#Main method call
main()