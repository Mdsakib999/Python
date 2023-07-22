#Q: Check Armstrong number or not?

userInput = int(input("Enter your number : "))      #enter 3 digit number
nums = userInput

a = nums % 10
nums = nums // 10
b = nums % 10
c = nums // 10

if (a**3)+(b**3)+(c**3) == userInput:           #formula
    print(userInput, "is a Armstrong number")
else:
    print(userInput, "is not a Armstrong number")


#if we take power 4 it will Narcissictic number (a**4)
