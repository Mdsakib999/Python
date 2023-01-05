#Count the number of each Vowel

from itertools import count


vowel = "aeiou"

my_str = "hey kemon acho tumra? ajk amar mon valo nai"

my_str = my_str.casefold()

count = {}.fromkeys(vowel, 0)

for char in my_str:
    if char in count:
        count[char]

print(count)