text = input("Enter a string: ")

new_text = ""

for ch in text:
    if ch == " ":
        new_text += "-"
    else:
        new_text += ch

print("Updated string:", new_text)