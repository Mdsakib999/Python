#accept a list of float number as an input from user

number =[]

for i in range(0, 3):
    print("enter number ", i)
    item = float(input("enter float number"))
    number.append(item)
print(number)