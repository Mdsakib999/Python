#Add two Matrices in Python.. or sum of twi Matrices..


a = [[12, 5, 3], [9, 4, 7], [11, 5, 2]]
b = [[5, 8, 9], [10, 5, 7], [9, 5, 8]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(a)):             #can add all for loop same line
    for j in range(len(a[0])):
        result [i] [j] = a[i][j] + b[i][j]

for x in result:
    print(x) 