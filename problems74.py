# Question 6


text = input("enter your text: ")
#text = "A man, a plan, a canal: Panama"

con_txt = text.replace(" ", "")
con_txt = ''.join(e for e in con_txt if e.isalnum())


if con_txt.lower() == con_txt[::-1].lower():  #using for loop
    print("true")
else:
    print("false")

