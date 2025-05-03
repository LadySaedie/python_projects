# Ask for the user's name and store it
fname = input("What’s your first name? ")

# Print a personalised greeting
print(f"Hello, {fname}! Welcome to Game On!")

# Start a mini adventure
print(f"{fname}, you’re in a forest. Do you go left or right?")
choice = input("Type 'left' or 'right': ")

# Respond based on the choice
if choice == "left":
    print("You find a treasure chest!")
else:
    print("A wild wolf appears and eats you!")