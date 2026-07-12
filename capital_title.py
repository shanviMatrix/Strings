text = input("Enter a sentence: ")

result = ""
new_word = True

for ch in text:
    if new_word and 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
        new_word = False
    else:
        result += ch

    if ch == " ":
        new_word = True

print(result)