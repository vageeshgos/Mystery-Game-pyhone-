


import time
import random

# Inventory to hold collected items
inventory = []

# Set the time limit (e.g., 120 seconds = 2 minutes)
time_limit = 120  # 120 seconds for the game
start_time = time.time()  # Record the start time

# Randomly place the key in either the left or right room
key_location = random.choice(["left", "right"])  # Key can be in either left or right room

# Function to check if the player has exceeded the time limit
def check_time():
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Time's up! You took too long. Game over!")
        exit()  # Ends the game if the time limit is exceeded
    else:
        # Display remaining time for the player
        remaining_time = int(time_limit - elapsed_time)
        print(f"Time remaining: {remaining_time} seconds")

# Define the starting room with a loop to avoid recursion
def start_room():
    while True:
        check_time()  # Check the time remaining
        print("\nYou are in a dark room with 2 doors.")
        print("One door is on the left, and the other is on the right.")
        
        # Player choice
        choice = input("Which door do you want to take? (left/right): ").lower()
        
        if choice == "left":
            bedroom("left")
        elif choice == "right":
            exit_room()
        else:
            print("Invalid choice. Try again.")

# Define the bedroom with parameter to indicate the room (left or right)
def bedroom(room_side):
    check_time()  # Check the time remaining
    print(f"\nYou have entered the {room_side} room.")
    
    # Check if this room has the key
    if room_side == key_location and "key" not in inventory:
        print("There is a shiny key with a joker keychain on the table.")
        choice = input("Do you take the key? (yes/no): ").lower()
        
        if choice == "yes":
            print("You picked up the key and went back to the dark room.")
            inventory.append("key")  # Add key to inventory
        else:
            print("You decided to leave the key and went back to the dark room.")
    else:
        print("There’s nothing useful here. You head back to the dark room.")

# Define the exit room
def exit_room():
    check_time()  # Check the time remaining
    print("\nYou entered a room with a locked door.")
    
    if "key" in inventory:  # Check if the player has the key
        print("You unlocked the door with the key and escaped! You win!")
        exit()  # End the game on a win
    else:
        print("The door is locked. You need to find the key.")
        choice = input("Type 'back' to return to the dark room: ").lower()
        if choice == "back":
            return  # Go back to start_room
        else:
            print("Invalid choice. Try again.")
            exit_room()

# Start the game
start_room()
