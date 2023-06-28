# patten peoblem ............


n = 5
for i in range(n):
    for j in range(i, n):        #(i, n) to see reverse (star ar jaigai space dita hobe)
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")     #(i+1)

    print()

