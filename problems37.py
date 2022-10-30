#HackerRank30 days of code || Day 6 || Python

n = int(input())
for i in range(n):
    s = input("string ")
    even = ""
    odd = ""
    for j in range (len(s)):
        if j % 2 == 0:
            even += s[j]
        else:
            odd += s[j]

    print(even,odd)