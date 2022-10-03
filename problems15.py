# Convert celsius to Fahrenheit ....

temp = float(input("Enter temperature : "))
unit = input("enter unit 'C' or 'F' which want to convert : ")

if unit == "c" or "C":
    new_temp = 9/5 * temp +32
    #print(temp,"celsius is equal to", new_temp, "Fahrenheit :", new_temp)
    print("temperature in Fahrenheit ",new_temp)

elif unit == "f" or "F":
    new_temp = 5/9 * (temp-32)
    #print(temp,"Fahrenheit is equal to", new_temp, "celsius :", new_temp)
    print("temperature in Celsius ",new_temp)

else:
    print("Invalid unit", unit)
