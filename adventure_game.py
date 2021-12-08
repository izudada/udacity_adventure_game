import time


cave_mode = False

def print_pause(string, num):
    print(string)
    time.sleep(num)


def enter_house():
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens and out steps a pirate.", 4)
    print_pause("Eep! This is the pirate's house!", 2)
    print("The pirate attacks you!", 2)

    user_house_option = int(input("Would you like to (1) fight or (2) run away? \n")) 
    if user_house_option == 2:
        print_pause("You run back into the field. Luckily, you don't seem to have been followed. \n", 4)


def enter_cave():
    """
        This section allows the user to peer into and enter the cave to retrieve a weapon
    """
    global cave_mode

    print_pause("You peer cautiously into the cave.", 2)
    if cave_mode == False:
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause("You discard your silly old dagger and take the sword with you.", 4)
        cave_mode = True
    else:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now. \n", 2)
    print_pause("You walk back out to the field.\n", 2)
            

def figth():
    print_pause("You approach the door of the house.", 3)
    print_pause("You are about to knock when the door opens and out steps a gorgon.", 4)
    print_pause("Eep! This is the gorgon's house!", 3)
    print_pause("The gorgon attacks you!", 2)
    print_pause("Would you like to (1) fight or (2) run away? \n")



# As the gorgon moves to attack, you unsheath your new sword.
# The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.
# But the gorgon takes one look at your shiny new toy and runs away!
# You have rid the town of the gorgon. You are victorious!


def game_intro():
    """
        This is to introduce the user to the scheme or game plan
    """

    print_pause("Rumor has it that a gorgon is somewhere around here, and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty (but not very effective) dagger. \n", 3)
    
    while True:
        print_pause("Enter 1 to knock on the door of the house.", 2)
        print_pause("Enter 2 to peer into the cave.", 2)
        print_pause("What would you like to do?", 3)
        user_choice = int(input("(Please enter 1 or 2.) \n")) 
        if user_choice == 2:
            enter_cave()
        elif user_choice == 1:
            enter_house()


game_intro()