#Fibonacci Sequence (sum of first two number)


#nterm = -5
nterm = int(input("Enter a number :"))

n1 = 0
n2 = 1
sum = 0

if nterm <= 0:
    print("Enter a positv number")

elif nterm == 1:
    print("Fibonacci sequence upto", nterm)
    print(n2)

else:
    print("Fibonacci sequence upto", nterm)

    while sum < nterm:
        print(n1, end=", ")
        nth = n1 + n2

        n1 = n2
        n2 = nth
        sum += 1

print()
