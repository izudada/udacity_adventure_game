import time
import random


cave_mode = False
enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
enemy = random.choice(enemies)
weapon = 'dagger'


def print_pause(string, num):
    print(string)
    time.sleep(num)


def enter_house():
    print_pause("You approach the door of the house.", 2)
    print_pause(f"You are about to knock when the door"
                "opens and out steps a {weapon}.", 4)
    print_pause(f"Eep! This is the {weapon}'s house!", 2)
    print("The pirate attacks you!", 2)

    user_house_option = int(input("Would you like to (1) fight "
                            "or (2) run away? \n"))
    if user_house_option == 2:
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed. \n", 4)
    elif user_house_option == 1:
        fight()


def enter_cave():
    """
        This section allows the user to peer into
        and enter the cave to retrieve a weapon
    """
    global cave_mode

    print_pause("You peer cautiously into the cave.", 2)
    if cave_mode is False:
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause(f"You discard your silly old {weapon}"
                    " and take the sword with you.", 4)
        cave_mode = True
    else:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now. \n", 2)
    print_pause("You walk back out to the field.\n", 2)


def game_intro():
    """
        This is to introduce the user to the scheme or game plan
    """
    print("\n")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                "and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause(f"In your hand you hold your trusty"
                "(but not very effective) {weapon}. \n", 3)

    while True:
        print_pause("Enter 1 to knock on the door of the house.", 2)
        print_pause("Enter 2 to peer into the cave.", 2)
        print_pause("What would you like to do?", 3)
        user_choice = int(input("(Please enter 1 or 2.) \n"))
        if user_choice == 2:
            enter_cave()
        elif user_choice == 1:
            enter_house()


def fight():
    print_pause(f"As the {enemy} moves to attack, you"
                "unsheath your new sword.", 4)
    print_pause("The Sword of Ogoroth shines brightly in your"
                "hand as you brace yourself for the attack.", 5)
    print_pause(f"But the {enemy} takes one look at your"
                "shiny new toy and runs away!", 4)
    print_pause(f"You have rid the town of the {enemy}."
                "You are victorious!", 4)

    repeat_game = input("Would you like to play again? (y/n)").lower()
    if repeat_game == 'y':
        game_intro()
    elif repeat_game == 'n':
        quit()


game_intro()
