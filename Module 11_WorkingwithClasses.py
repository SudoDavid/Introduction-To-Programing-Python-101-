class Party(object):
    #initialize variables/objects
    def __init__ (self,):
        self.max_guests = 15
        self.cake = "vanilla"
        self.icecream = "strawberry"
        self.baloons = 15
        self.plates = 15

    #put data passed from program into class instance
    def set_guests(self, numguests):
        self.max_guests = numguests
    #set cake
    def set_cake(self, caketype):
        self.cake = caketype
    #set icecream
    def set_icecream(self, icecream):
        self.icecream = icecream
    #set baloons
    def set_baloons(self, baloons):
        self.baloons = baloons
    #set plates
    def set_plates(self, plates):
        self.plates = plates
    
   #return data to program from class instance
    def get_icecream(self):
        return self.icecream
    def get_cake(self):
        return self.cake
    def get_guests(self):
        return self.max_guests
    def get_baloons(self):
        return self.baloons
    def get_plates(self):
        return self.plates

    #calculations
    def howmanycakes(self):
        buycakes = int(self.max_guests)/8
        print(buycakes)
        return buycakes

p1 = Party()
p1.howmanycakes()