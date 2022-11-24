#Shuffle Duck of card using random module...?
# Simple game


import itertools, random

deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))

random.shuffle(deck)

#draw 5 cards
print("You got :")
for i in range(5):      #I can increase changing range value
    
    print(deck[i][0], "of", deck[i][1])
