#find the sum of Natural Number 

num = int(input("Enter number : "))

if num < 0:
    print("Enter positive number!!")

else:
    sum = 0
    for i in range(num+1):  #while (num > 0);
        sum += i
        num -= 1
    print(sum)

"""
sum = num * (num + 1)/2
print(sum)
"""    