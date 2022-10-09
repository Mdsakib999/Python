#calculate HCF and LCM 

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

while a % b != 0:
    rem = a % b
    a = b
    b = rem
HCF = rem
print("HCF is", rem)

LCM = (a*b)/HCF
print("LCM is", LCM)



"""
for i in range(1, a+1):
    if (a % i ==0) and (b % i==0):
        print("HCL IS ",i)
"""
