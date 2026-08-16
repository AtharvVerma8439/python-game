print("Welcome to the Mysterious Forest!")
player_name = input("What is your name, brave adventurer? ")

print("\nGood luck, " + player_name + ". Your journey begins now.")

print("\nYou stand at a fork in the dirt path.")
choice1 = input("Do you go 'left' into the dark cave, or 'right' towards the glowing cabin? ")

if choice1 == "left":
    print("\nYou step into the cave and wake up a sleeping dragon. Chomp! Game Over.")
elif choice1 == "right":
    print("\nYou knock on the cabin door. A wizard gives you a chest of gold. You win!")
else:
    print("\nYou stand there confused until night falls. The forest gets too dark. Game Over.")
