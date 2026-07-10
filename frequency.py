text = input("Enter a string: ")
character = input("Enter the character to find: ")

count = 0

for ch in text:
    if ch == character:
        count += 1

print("Frequency of", character, "is", count)