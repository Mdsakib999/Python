#Menu driven program in Python.

userInput = input('''
Hey welcome
What do you want convert.
1. convert cm to inch
2. convert usd to Tk
3. convert celsius to Fahrenhit
4. convert km to mile
''')

if userInput == '1':
    cm = float(input("Enter cm : "))
    inch = cm * 0.394
    print(cm,"cm =", inch,"inc")

elif userInput == "2":
    usd = float(input("enter amount in USD : "))
    taka = usd * 90
    print(usd,"$ =", taka,"tk")

elif userInput == "3":
    f = float(input("Enter temperature in Fahrenhit : "))
    c = 0.56 * (f-32)
    print(f, "Fahrenhit =", c, "celsius")

elif userInput == "4":
    km = float(input("Enter km : "))
    mile = km * 0.621
    print(km,"km =", mile,"mile")

else:
    print("Enter a valid number ")
