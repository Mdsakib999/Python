#Remove duplicate character from given string.

def remove_dupli(string):
    result = ""
    for i in string:
        if i not in result:
            result += i
    return result


user_inp = input("what is your name my boy. saki sakib Wht you are so upset")
no_dupli = remove_dupli(user_inp)
print("without duplicate", no_dupli)