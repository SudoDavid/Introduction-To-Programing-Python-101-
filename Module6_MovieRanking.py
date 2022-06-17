#David Piro
#6/16/2022
#Module 6
#Movie Rating Tracking



#Average function
def Average(movie_rating):
    return sum(movie_rating) / (len(movie_rating)-1)

x = 0
user_input = True
while(user_input == True):
#accept user input for movie rating
    movie_list = 'Titan A.E.'
    print("What would you rate the following movie?", movie_list)
    movie_rating = [x]
    #ask for next rating
    y = int(input("Please enter a movie rating between 0 and 4. \n"))
    #add next rating to the list
    movie_rating.insert(x, y)

    #continue to next user
    next_user = int(input("Do you or another user want to enter a rating for a movie? Please enter a negative number to quit. \n"))
    if (next_user > 0):
        user_input = True
    else:
        average = Average(movie_rating)
        print("The average of the movie ratings for", movie_list, average)
        user_input = False
