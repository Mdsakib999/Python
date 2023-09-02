#problems12 
#Fibonacci Sequence using function


def re_fibo(n):
    if n <= 1:                     #if you want see negative value use n < 1
        return n
    else:
        return(re_fibo(n-1) + re_fibo(n-2))

nth = 10

if nth <= 0:
    print("Enter a positive number :")
else:
    print("Fibonacci seq: ");
    for i in range(nth):
        print(re_fibo(i))           #end=", "
