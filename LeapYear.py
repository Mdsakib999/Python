# Default function to implement conditions to check leap year  
""""
def CheckLeap(Year):   
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
   
  else:  
    print ("Given Year is not a leap Year")  
 
Year = int(input("Enter the number: "))  

CheckLeap(Year)
"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return leap
    elif (year % 4 == 0):
        return True
    else:
        return False 
    
    return leap
year = int(input())
print(is_leap(year))

"""
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input())
print(is_leap(year))
"""
"""
if year % 4 == 0:
    print("leap year)
else:
    print("not leap year")
"""