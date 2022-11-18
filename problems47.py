#Python Program to Count Most Frequent Words in a File?
# Add a file from your local machine.



words = []
with open("blog.html", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top5 = counts.most_common(5)
print(top5)
