#sum and reverse of a 3 digit number given by user


num = int(input("enter a three disit number :"));

a = num % 10        #345 % 10 = 5
num = num // 10     #345 // 10 =034
b = num % 10        #num b =34 % 10 = 4
c = num // 10       #c = 34// 10 = 3

sum = a+b+c
print(sum)

rev = 100*a + 10*b+ c
print(rev)
