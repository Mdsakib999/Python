#Convert Decimal to Binary using Recursion

def dec_to_bin(n):
    if n > 1:
        dec_to_bin(n//2)
    print(n % 2, end="")


dec = int(input("Enter a Decimal number : "))        #3.2, 50.2 float number is not possible to convert

dec_to_bin(dec)
print();
