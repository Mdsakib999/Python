#take 3 angle from user and check make triangle or not

a = int(input("Enter angle a :"))
b = int(input("Enter angle b :"))
c = int(input("Enter angle c :"))

if a + b + c ==180 and a!=0 and b!=0 and c!=0:
    print("possible to make triangle")
else:
    print("Not possible")