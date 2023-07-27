#OPPs problems solution (calculate discount)?


class Laptop:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def cal_discount(self, prcentage):
        offfer_price = (prcentage/100)*self.price
        return self.price - offfer_price

laptop1 = Laptop("Core i5", "Dell", 55000)
print("Price after discount ",laptop1.cal_discount(5))
      
