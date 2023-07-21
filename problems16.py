#Calculate the Sum and Average of given number?

len = int(input("How many number do you want to enter : "))
num = []

for i in range(0, len):
    ele = int(input("Enter element : "))
    num.append(ele)

sum_num = sum(num)
print("sum of number : ", sum_num)

avg = sum_num/len
print("Average", round(avg,2))





"""
len = int(input("how many number want to adde : "))

sum = 0

for i in range(0, len):
    ele = int(input("Enter element : "))
    sum += ele

print("Sum =", sum)
avg = sum / len
print("Average =", avg)
"""
