# Check a string weather palindrome or not.
# Palindrome means: A string which is same, when read forward or backwards. exp "dad"


my_string = input("Enter your string: ")

my_string = my_string.casefold()

rev_str = reversed(my_string)

if list(my_string) == list(rev_str):
    print(my_string, "is palindrome.")
else:
    print("It's not palindrome.")