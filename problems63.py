#Write a python code to Remove punctuation from string.

from string import punctuation


#punctuation = """!@#$%&*()_+:\;,./{?}[]"'"""

myString = "hi, how are u?... i'm fine()"

no_punc = ""

for char in myString:
    if char not in punctuation:
        no_punc = no_punc + char

print(no_punc);
