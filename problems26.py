# Print the Fibonacci Sequence in Python?

number = int(input("Enter number : "))

n1 = 0
n2 = 1
count = 0

if number <= 0:
    print("Enter positive number : ")

else:
    while count <= number:
        print(n1, end=", ")
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1

print()
