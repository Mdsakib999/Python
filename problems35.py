# Find highest common factor(H.C.F) OR Greatest common divisor(G.C.D)

def count_hcf(x, y):
    if x > y:
        small = y
    else:
        small = x
    
    for i in range(1, small+1):
        if ((x % i == 0) and (y % i ==0)):
            hcf = i
    
    return hcf


num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))

print("The H.C.F Of", num1, "and", num2, "is", count_hcf(num1, num2))




#Another way
"""
num1 = 54
num2 = 24

while(num2):
    num1, num2 = num2, num1 % num2
print(num1)
"""



"""
a = 10
b = 40
if a > b:
    small = b

else:
    small = a

for i in range(1, small+1):
    if (a % i ==0) and (b % i == 0):
        hcf = i
    
print(hcf)
"""
