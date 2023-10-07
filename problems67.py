#Write a python program to calculate Interest counter.

main_amount = int(input("How money you borrowed? "))
interest_rate = float(input("Interest rate: "))
time = float(input("Total time in year: "))

interest = main_amount * (interest_rate / 100) * time

print("Simple Interest is", interest)

total_amount = main_amount + interest

print("Total amount with Interest is", total_amount);








"""
#Compound interest counter......

main_amount = int(input("How money you borrowed? "))
interest_rate = float(input("Interest rate: "))
time = float(input("Total time in year: "))

interest = main_amount * ((1 + interest_rate/100)**time)

print("compound interest is: ", interest)
"""
