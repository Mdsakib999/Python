#Number system Conversion.
#decimal to octal, binary and haxadecimal

from unicodedata import decimal


num = int(input("Enter a decimal number : "))

print(bin(num),"in bianry")
print(oct(num),"in Octal")
print(hex(num),"in haxadecimal")
