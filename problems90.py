#Find the factorial of given number...........?

def factrial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)

factrial(5)


"""
# Another way

n = 6
fact = 1
for i in range(1,n+1):
    fact = fact*i
    
print(fact)
"""
