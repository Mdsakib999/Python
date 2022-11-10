#Find the factorial of given number?

def factor(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

num = int(input("enter a number : "))

print(factor(num))
