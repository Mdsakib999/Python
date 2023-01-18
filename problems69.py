'''
Question:
You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40
'''


#your code goes here
text = input("Enter the text: ")

l = input("Enter the letter: ")

sum = 0

for i in text:
    if i == l:
        sum += 1

per = (sum / len(text))*100

print(int(per),"%")
