#print all prime number in range

lower = 900         # lower = int(input("Enter a lower number"))
upper = 1000

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i ==0):
                break
        else:
            print(num)
