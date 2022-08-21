#import random
#print(random.randint(0,9))

import random

gus = int(input("Guess a number: "))

number = random.randint(0, 5)
if gus == number:
    print("Wooow!!!, you are right")
else:
    print("Sorry!!! you are wrong")
    
print("The number is",number)
