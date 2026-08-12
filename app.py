text = input("Enter a sentence: ")

# Count words
words = text.split()
word_count = len(words)

# Count numbers
number_count = 0

for word in words:
    if word.isdigit():
        number_count += 1

# Count characters
character_count = len(text)

print("\n--- Result ---")
print("Words:", word_count)
print("Numbers:", number_count)
print("Characters:", character_count)