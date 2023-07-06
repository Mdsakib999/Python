#opp practice (calculate the aria of Triangle)


class Triangle:
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight

    def cal_aria(self):
        area = 0.5 * self.base * self.hight
        print("Aria of tringle", area)
        
t1 = Triangle(20, 30)
t1.cal_aria()

t2 = Triangle(10, 20)
t2.cal_aria()
