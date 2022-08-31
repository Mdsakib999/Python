#How to calculate profit or loss of any product??

a = float(input('Enter buying cost :'))
b = float(input('Enter selling cost :'))

if a < b:
    amount = b - a
    print ('profit', amount)
else:
    amount = a - b
    print('loss', amount)
