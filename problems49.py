#Index of the Maximum Value in a Python List?

def maximum(x):
    maximum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] > x[maximum_index]:
            maximum_index = current_index
        current_index = current_index + 1
    return maximum_index

a = [76, 45, 20, 70, 65, 150, 54]
print("Maximum value index", maximum(a))
print("Maximum value of list", max(a))