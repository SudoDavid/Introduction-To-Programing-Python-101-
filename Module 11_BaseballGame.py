#David Piro
#Last Updated 7/26/2022
#Created 7/26/2022
#######################
class BaseballGame(object):
    def __init__(self, nameOne, nameTwo, scoreOne, scoreTwo):
        self.nameOne = nameOne
        self.nameTwo = nameTwo
        self.scoreOne = scoreOne
        self.scoreTwo = scoreTwo
        
    #setters
    def set_name(self, name):
        self.name = name
    def set_score(self, score):
        self.score = score
    
    #getters
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    
    def declareWinner(self):
        if self.scoreOne > self.scoreTwo:
            print("The Winner for this game is the:" )
            print(self.nameOne)
            return self.nameOne
        elif self.scoreOne < self.scoreTwo:
            print("The Winner for this game is the: " )
            print(self.nameTwo)
            return self.nameTwo
        else:
            print("Tie Ball GAME!")
            return self.nameOne


s1 = input("Please enter the score for team1:")
s2 = input("Please enter the score for team2:")
Game1 = BaseballGame('Yankees', 'RedSox', s1, s2)
Game1.declareWinner()

s1 = input("Please enter the score for team1:")
s2 = input("Please enter the score for team2:")
Game2 = BaseballGame('Yankees', 'RedSox', s1, s2)
Game2.declareWinner()

s1 = input("Please enter the score for team1:")
s2 = input("Please enter the score for team2:")
Game3 = BaseballGame('Yankees', 'RedSox', s1, s2)
Game3.declareWinner()

