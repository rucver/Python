string=input("Enter a number to be checked (for Palindrome):")
rev = ""
for char in range(0, len(string)):
    rev = string[char]+rev
    print(rev)
if (rev==string):
    print("the input string IS A PALINDROME")
else:
    print("the input string IS NOT A PALINDROME")




