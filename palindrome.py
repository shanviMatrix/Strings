text = input("Enter a string: ")

reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")