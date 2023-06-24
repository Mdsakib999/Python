#print love with given input 

n = 6
m = 7
for i in range(n):
    for j in range(m):
        if (i ==0 and j % 3 !=0) or (i==1 and j % 3 ==0) or (i-j == 2) or (i+j == 8):
            print("*", end="  ")
        else:
            print(" ", end="  ")
        
    print()

    """
    n = 6
m = 7
print("how programmer show love....")
for i in range(n):
    for j in range(m):
        if (i ==0 and j % 3 !=0) or (i==1 and j % 3 ==0) or (i-j == 2) or (i+j == 8):
            print("*", end="  ")
        elif (i == 2 and j == 3):
            print(" ", end="")
        else:
            print(" ", end="  ")
        
    print()
    """
