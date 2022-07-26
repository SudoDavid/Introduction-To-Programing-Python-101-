#David Piro
#Last Updated 7/26/2022
#Created 7/26/2022
#######################
class Motorcycle(object):
    def __init__(self, max_speed, speed, sidecar):
        self.max_speed = max_speed
        self.speed = speed
        self.sidecar = sidecar

    #set max_speed
    def set_max_speed(self, max_speed):
        self.max_speed = max_speed
    #set speed
    def set_speed(self, speed):
        self.speed = speed
    #set sidecare
    def set_sidecar(self, sidecar):
        self.sidecar = sidecar

    def get_max_speed(self):
        return self.max_speed
    def get_speed(self):
        return self.speed
    def get_sidecar(self):
        return self.sidecar
#Write an accelerate method. Return a 1 if the motorcycle  is going too fast.  
# Return a 2 if the motorcycle is ok.  Print a message in the main program  
# so the following is displayed when the Motorcycle tries to accelerate beyond its maximum speed: "This motorcycle cannot go that fast".

    def hassidecar(self):
        if self.sidecar == True:
            print("This motorcycle has a sidecar.")
        else:
            print("This motorcycle does not have a sidecar.")

    def accelerate(self):
        if self.speed > self.max_speed:
            print("This motorcycle cannot go that fast")
            return 1
        else:
            print("This motorcycle can go that fast")
            return 2
    def printspeed(self):
        print(self.speed)

m1 = Motorcycle(90, 65, True)
m1.printspeed()
m1.accelerate()
m1 = Motorcycle(90, 95, True)
m1.printspeed()
m1.accelerate()
m1.hassidecar()

m2 = Motorcycle(85, 60, False)
m1.printspeed()
m2.accelerate()
m2 = Motorcycle(85, 80, False)
m2.printspeed()
m2.accelerate()
m2.hassidecar()

       


        
