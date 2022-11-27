#Sum of Natural number using Recursing???

def rec_sum(n):
    if n <= 1:
        return n
    else:
        return n + rec_sum(n - 1)

num = 10

if num <= 0:
    print("Enter a positive number :")
else:
    print("The sum is:", rec_sum(num))