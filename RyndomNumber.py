#Guess a number in the range.

#print a number rendomly between given range.



import random

gus = int(input("Guess a number: "))

number = random.randint(0, 5)
if gus == number:
    print("Wooow!!!, you are right")
else:
    print("Sorry!!! you are wrong")
    
print("The number is",number)
