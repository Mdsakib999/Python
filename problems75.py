#question 2


def longest_comm_prefix(text):
    comm_prefix = ""
    for char in zip(*text):
        if len(set(char)) == 1:
            comm_prefix += char[0]
        else:
            break

    return comm_prefix

given_text = longest_comm_prefix(["school","schedule"])
print(given_text)

