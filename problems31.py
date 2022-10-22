#Findd number divisible by giver number in list

my_list = [5, 10, 12, 30, 40]

num = 5

result = list(filter(lambda X:(X % num ==0), my_list))

print("Numbers divisible by",num,"are",result)