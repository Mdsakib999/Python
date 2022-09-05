#vowle count

def vou_con(sentence):
    vowle = ['a', 'e', 'i','o', 'u', 'A','E', 'I', 'O', 'U']
    count = 0
    for cher in sentence:
        if cher in vowle:
            count += 1
    return count

print(vou_con('hi ame tmak valobase'))