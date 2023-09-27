#Multiply tow Matrices...

x = [[5, 8, 16], [8, 10, 3], [7,5,22]];
y = [[2, 7, 6], [18, 1, 9], [5,15,2]];

result = [[0,0,0], [0,0,0], [0,0,0]];

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]


for r in result:
    print(r);
