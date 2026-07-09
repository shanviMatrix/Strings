text = input("Enter a string: ")

new_text = ""

for ch in text:
    if ch != " ":
        new_text += ch

print("String without spaces:", new_text)