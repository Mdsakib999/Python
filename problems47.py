#Python Program to Count Most Frequent Words in a File?

words = []
with open("blog.html", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top5 = counts.most_common(5)
print(top5)
