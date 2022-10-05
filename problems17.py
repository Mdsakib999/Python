#sum of given list

def sum_list(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

nums = [5, 15, 20, 9, 18]  

total_sum = sum_list(nums)
print("Sum of total element : ", total_sum)


"""
shortcut
len = int(input("How many element do you want to enter : "))
nums = []
for i in range(0, len):
    ele = int(input("enter the number : "))
    nums.append(ele)

print("nums =",nums)
sum_ele = sum(nums)
print("Sum of total element : ", sum_ele)

"""