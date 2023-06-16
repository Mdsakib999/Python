#---------inharetace in python-------------
#OOPs problems

class Vhecale:
    def __init__(self, cost, milage):
        self.cost = cost
        self.milage = milage

    def show_dls(self):
        print("cost is", self.cost)
        print("milage is", self.milage)
        print("I am a vhecile")

v1= Vhecale(100, 5000)
v1.show_dls()

        #child class inharat 
class Car(Vhecale):
    def __init__(self, cost, milage, color, hp):
        super().__init__(cost, milage)
        self.color = color
        self.hp = hp


    def show_dls_car(self):
        print("I am car")
        print("Colorr of car", self.color)
        print("hourse power", self.hp)
        
c1= Car(200, 8000, "blue", 32)
c1.show_dls()
c1.show_dls_car()
