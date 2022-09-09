#Calculate Volume of Cylinder

r = float(input("Enter radius :"))
h = float(input("Enter hight :"))

v = 3.1416*(r**2)*h
print("volum is %.2f:" %v)

cost =v/1000 * 40
print("Your cost is :", cost, "$")