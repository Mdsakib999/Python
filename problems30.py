# Display the power of given number range??

num = 10        #can take input from usear 

result = list(map(lambda X: 2**X, range(num+1))) #important

print("total terms is : ", num);

for i in range(num+1):
    print("2 rised to power", i, "is", result[i]);



"""
num = 5

for i in range(num):
    print("2 terms of power", i, "is", i**2);
"""
