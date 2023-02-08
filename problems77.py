# Question 1


roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def romanToDecimal(a: str) -> int:
    value = 0

    for i in range(len(a)-1,-1,-1):
        number = roman[a[i]]
        if 4* number < value: value -= number
        else: 
            value += number
    return value


roman_value = romanToDecimal("V")
print("Integer", roman_value) 



# Alternative way 

'''
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def romanToDecimal(str):
    result = 0
    i = 0

    while (i < len(str)):
        x1 = value(str[i])

        if (i + 1 < len(str)):
            x2 = value(str[i + 1])

            if (x1 >= x2):
                result = result + x1
                i = i + 1
            else:
                result = result + x2 - x1
                i = i + 2
        else:
            result = result + x1

    return result

#roman_num= romanToDecimal("x")
#print(roman_num)



# take input from usear

roman_num = input("roman number Upper case: ")
print('Integer: ',romanToDecimal(roman_num))   

'''

