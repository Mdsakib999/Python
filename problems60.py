#Transpose Matrix in Python..

#using nested loop
x = [[12, 7], [4, 5], [3, 8]]

result = [[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for a in result:
    print(a)





"""
# Aulternative way


x = [[12, 7], [4, 5], [3, 8]]

result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

for r in result:
   print(r)

"""
