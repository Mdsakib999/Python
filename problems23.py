#Q: Calculate the factorial of given number of user?

num = int(input("Enter number : "))
user_inp = num
i = 1

if num >= 0:
    while num >= 1:
        i = i * num
        num -= 1
    print("Factorial of",user_inp, "is", i)

else:
    print("enter a positive number")
