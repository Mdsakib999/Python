#Multiplication Table using for and while loop.

x = int(input("Enter a number : "))

for i in range(1, 11):
    #a = x * i
    
    print(x, "x", i, "=", x*i)  # x*i ar jaigai a deao kora jabe
    i += 1


"""
usuing while loop

n = 3
i = 1
while i < 11:
    print(n, "x", i, "=", n*i)
    i += 1
"""
