#FizzBuzz in python

n = int(input("Enter a number : "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz") 
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


"""
n = 16
for i in range(1, n):
    if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
    elif i % 3 == 0:
            print("Fizz")
    elif i % 5 == 0:
            print("Buzz")
    elif i % 3 != 0 and i % 5 != 0:
            print(i)
    else:
        print("not")
        
    """