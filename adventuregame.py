import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself standing in front of two doors.")
    print("Do you want to go through the 'left' door or the 'right' door?")
    
def choose_door():
    while True:
        choice = input("> ").lower()
        if choice == "left":
            return "left"
        elif choice == "right":
            return "right"
        else:
            print("Invalid input. Please choose 'left' or 'right'.")

def left_door():
    print("You enter the left door and find a treasure chest.")
    print("Do you want to 'open' it or 'leave' it?")
    choice = input("> ").lower()
    if choice == "open":
        print("Congratulations! You found a treasure chest full of gold.")
    else:
        print("You leave the treasure behind and continue your adventure.")

def right_door():
    print("You enter the right door and find a hungry lion!")
    print("Do you want to 'fight' the lion or 'run' away?")
    choice = input("> ").lower()
    if choice == "fight":
        print("The lion is too powerful. You didn't survive.")
    else:
        print("You wisely run away and escape from the lion's den.")

def main():
    intro()
    door_choice = choose_door()
    
    if door_choice == "left":
        left_door()
    else:
        right_door()
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
