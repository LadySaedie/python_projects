# Ask for the user's name and store it
fname = input("What’s your first name? ")

# Print a personalised greeting
print(f"Hello, {fname}! Welcome to Game On!")

# Start the adventure by describing the scene and asking for a choice
print(f"{fname}, you’re in a forest. Do you go left or right?")

# Store the user's choice ('left' or 'right') in the variable 'choice'
choice = input("Type 'left' or 'right': ")

if choice.lower() == "left":
    print(f"{fname}! You've found the buried treasure chest!")
elif choice.lower() == "right":
    print(f"{fname}! RUN! A wild wolf is about to eat you!")
else:
    print(f"{fname}, you wrote: '{choice}'. Please type only 'left' or 'right'. Nothing else")