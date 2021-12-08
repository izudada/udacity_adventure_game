import time

def print_pause(string, num):
    print(string)
    time.sleep(num)


def game_intro():
    print_pause("Rumor has it that a gorgon is somewhere around here, and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n \n", 3)
    print_pause("Enter 1 to knock on the door of the house.", 2)
    print_pause("Enter 2 to peer into the cave.", 2)
    print_pause("What would you like to do?", 3)


def enter_cave():
    print_pause("You peer cautiously into the cave.", 2)
    print_pause("It turns out to be only a very small cave.", 2)
    print_pause("Your eye catches a glint of metal behind a rock.", 2)
    print_pause("You have found the magical Sword of Ogoroth!", 2)
    print_pause("You discard your silly old dagger and take the sword with you.", 4)
    print_pause("You walk back out to the field. \n \n", 2)
    print_pause("Enter 1 to knock on the door of the house.", 2)
    print_pause("Enter 2 to peer into the cave.", 2)
    print_pause("What would you like to do?", 2)

    user_cave_action = int(input("(Please enter 1 or 2.)"))



def game_action():
    user_choice = int(input("(Please enter 1 or 2.)"))

    if user_choice == 2:
        enter_cave()

game_intro()