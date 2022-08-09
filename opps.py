class Employe:
    def __init__(self, name, age, selery):
        self.name = name
        self.age = age
        self.selery = selery

    def employ_det(self):
        print("name of employ", self.name)
        print("Age of emp", self.age)
        print("selery of emp", self.selery)
        

e1 = Employe("sakib", 20, 10000)

e1.employ_det()

"""
class Phone:
    def set_color(self,color):
        self.color = color
    def show_color(self):
        return self.color

    def make_call(self):
        print("makr a call")
    def play_game(self):
        print("play a game")
p= Phone()

p.set_color('blue')
p.show_color()

p.make_call()

#p1.play_game()

"""