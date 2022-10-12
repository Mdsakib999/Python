#Armstrong number in range

lower = 100
higher = 1000

for i in range(lower, higher+1):
    order = len(str(i))

    sum = 0

    num = i

    while num > 0:
        digit = num % 10
        sum += digit**order
        num //= 10
    if i == sum:
        print(i)
        #break
else:
    print("No more Armstrong number in this range!!!")