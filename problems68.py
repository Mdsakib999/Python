#Compound Interest

def compound_int(p, r, t):
    interest = main_amount*(1 + (interest_rate / 100)**time)
    return interest



main_amount = int(input("Enter the money you borrow: "))

interest_rate = float(input("Enter the interest rate: "))

time = float(input("Enter time in year: "))

total = compound_int(main_amount, interest_rate, time)
print("compound interest is:",total)



'''
from tokenize import Double


main_amount = int(input("Enter the money you borrow: "))

interest_rate = float(input("Enter the interest rate: "))

time = float(input("Enter time in year: "))

compound_int = main_amount*(1 + (interest_rate / 100)**time)

print("Compound interest: ", compound_int)
'''