'''Question
Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.

'''

s1 = input("Enter 1st line: ")
s2 = input("Enter 2nd line: ")

sum = 0

l1 = s1.split()
l2 = s2.split()

for i in l1:
    for j in l2:
        if i == j:
            sum += 1


print(sum)
