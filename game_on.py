fname = input("What’s your first name? ")
print(f"Hello, {fname}! Welcome to Game On!")

print(f"{fname}, you’re in a forest. Do you go left or right?")
choice = input("Type 'left' or 'right': ")

if choice.lower() == "left":
   print(f"{fname}, you found a chest! Open it or run?")
   choice2 = input("Type 'open' or 'run': ")
   if choice2.lower() == "open":
       print(f"{fname}, it’s full of gold!")
   else:
       print(f"{fname}, you escaped safely!")
elif choice.lower() == "right":
    print(f"{fname}! RUN! A wild wolf is about to eat you!")
else:
    print(f"{fname}, you wrote: '{choice}'. Please type only 'left' or 'right'. Nothing else")