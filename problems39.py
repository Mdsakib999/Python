#Python Program to Count Capital Letters in a File?
#Add a file


with open("blog.html") as file:
    count = 0
    text = file.read()
    for i in text:
        if i.isupper():
            count += 1
    print(count)

    list_num = {}
