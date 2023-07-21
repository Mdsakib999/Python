#Find rots of a Quadratic Equation(ax**2 + bx + c = 0)

import cmath

a = 50
b = 60
c = 40

#calculate the discriminant

d = (b**2) - (4*a*c)

#find two solution
r1 =(-b-cmath.sqrt(d))/(2*a)
r2 =(-b+cmath.sqrt(d))/(2*a)
print("Roots are :", r1, r2)
