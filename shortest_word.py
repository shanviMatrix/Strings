sentence = input("Enter a sentence: ")

current = ""
shortest = ""

for ch in sentence:
    if ch != " ":
        current += ch
    else:
        if shortest == "" or len(current) < len(shortest):
            shortest = current
        current = ""

# Check the last word
if shortest == "" or len(current) < len(shortest):
    shortest = current

print("Shortest word:", shortest)
print("Length:", len(shortest))