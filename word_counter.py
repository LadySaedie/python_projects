# Prompt the user to type a sentence or paragraph and store their input as a string in the variable 'text'
text = input("Enter a sentence or paragraph and hit Enter: ")

# Split the input string into a list of words, using spaces as the separator, and store the list in 'words'
words = text.split()

# Print the number of words in the list, using an f-string to format the output nicely
print(f"Word count: {len(words)}")