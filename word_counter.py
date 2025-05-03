# Prompt the user to type a sentence or paragraph and store their input as a string in the variable 'text'
text = input("Enter a sentence or paragraph and hit Enter: ")

# Split the input string into a list of words, using spaces as the separator, and store the list in 'words'
words = text.split()

# Print the number of words in the list, using an f-string to format the output nicely
print(f"Word count: {len(words)}")
# Print the number of unique words by converting the list to a set
print(f"Unique words: {len(set(words))}")
# Print the total characters, including spaces
print(f"Character count: {len(text)}")