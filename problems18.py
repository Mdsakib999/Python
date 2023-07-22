#Find the largest number of the list?

def large_num(nums):
    largest = nums[0]
    for i in nums:
        if largest < i:
            largest = i
    return largest

nums = [9,40,25,8,30]

largest = large_num(nums)       #largest = max(nums) (shortcut)

print("Large of the list is : ", largest)
