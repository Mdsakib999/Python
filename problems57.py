#Find Factorial of number using Recursion...

def rec_factorial(n):
    if n == 1:
        return n
    else:
        return n * rec_factorial(n-1)

num = 10

if num <= 0:
    print("Enter a positive number : ")
else:
    print("The factorial of", num, "is", rec_factorial(num))
