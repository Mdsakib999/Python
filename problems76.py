#Find the longest stake of an array?

# question 7

def longest_cons(x):
    long_stk = 0

    for i in x:
        present_number = i
        present_stk = 1

        while present_number + 1 in x:
            present_number += 1
            present_stk += 1

        long_stk = max(long_stk, present_stk)

    return long_stk

given_arr = [1,2,5,4,3,6,85,4,5,]
print(longest_cons(given_arr))

