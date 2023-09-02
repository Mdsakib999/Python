#Write code calculate the execution time of python program?

from time import time
start = time()

#create acronyms prigram
word = "Sakib Vai"
text = word.split()
a = " "

for i in text:
    a = a+str(i[1]).upper()
print(a);

end = time()
exe_time = end - start
print("Execution time ", exe_time);
