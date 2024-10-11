
from room import Room
from charachter import Enemy

# Initialize rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

# Create an enemy character
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi, I'm Dave, and I totally won't eat your brains!")
dave.set_weakness("cheese")
dining_hall.set_charachter(dave)

# Set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decor")

# Link rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Start the game in the kitchen
current_room = kitchen

# Game loop
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_charachter()
    
    if inhabitant is not None:
        inhabitant.describe()

    # Take player input
    command = input("> ").lower()

    if command == "talk" and inhabitant is not None:
        # If 'talk' command is entered and there is someone in the room, talk to them
        inhabitant.talk()

    elif command == "fight" and inhabitant is not None:
        # If 'fight' command is entered and there is someone in the room, ask the player for an item to fight with
        print("What will you fight with?")
        fight_with = input("Enter item: ").lower()
        if not inhabitant.fight(fight_with):
            print("Game over. You have been defeated!")
            break  # End the game if the player loses the fight
        else:
            print("You won the fight!")

    else:
        # If the input is not 'talk' or 'fight', assume it's a movement command
        current_room = current_room.move(command)
