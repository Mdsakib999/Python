#opps problems

class SmartDiv:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def recharge(self):
        print("hey sakib....")
        print("What do you want buy")

class Watch(SmartDiv):
    def __init__(self, brand, price, has_gps):
        SmartDiv.__init__(self, brand, price)
        self.count = 0
        self.has_gps = has_gps

my_watch = Watch("xiaome", 2000, False)

print(my_watch.price)
my_watch.recharge()

