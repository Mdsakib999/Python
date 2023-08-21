#Find the Duplicate Values?


def find_duplicates(x):

    length = len(x)

    duplicates = []

    for i in range(length):

        n = i + 1

        for a in range(n, length):

            if x[i] == x[a] and x[i] not in duplicates:

                duplicates.append(x[i])

    return duplicates

names = ["Sakib", "Rakib", "Mamun", "Sakib", "Rocky", "Banti", "Rocky"]

print("Given list =", names)
print("Duplicate values = ", find_duplicates(names))
