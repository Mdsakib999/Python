# Object oriented (opps) related problem.....
# oppAbstrraction


from abc import ABC,abstractmethod

#example of abastraction
class Shape:
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight
    @abstractmethod
    def cal_aria(self):
        pass
        
class Triangle(Shape):
    def cal_aria(self):
        area = 0.5 * self.base * self.hight
        print("Area of Tringle :", area)

class Ractaggal(Shape):
    def cal_aria(self):
        area = self.base * self.hight
        print("Area of Ractaggal :", area)



t1 = Triangle(10, 30)
t1.cal_aria()

t2 = Ractaggal(10, 20)
t2.cal_aria()
