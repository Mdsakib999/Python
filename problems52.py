#Find last common multiple(LCM) of two number???

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = 54
num2 = 24
print("The LCM of", num1, "and", num2,"is : ", lcm(num1, num2));




"""
# way 2

def gcd(x, y):

    while(y):
        x,y = y, x % y
    return x

def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm;


n1 = 54
n2 = 24

print(lcm(n1, n2));

"""
