"""
n = 5
p = 5

for i in range(n):
    for j in range(i,n):
        print(p, end="")
    p -= 1
    print()
"""
n = 5
P = 1
for i in range(n-1):        #whin need to print hill (n) and half code
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(P, end=" ")
    for j in range(i+1):
        print(P, end=" ")
    P += 1
    print()