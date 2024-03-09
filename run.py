# Imported Modules
import os
import time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

# Inventory for items picked up in the game
inventory = []

# Inventory for riddle notes picked up in the game
riddle = []

# notes/clues picked up from in the game
notes = []


# Clear the screen in a cross-platform manner
def clear_screen():
    """
    Function to clear screen after each new scene in the game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033c", end="")


# Clues function that will show inventory, riddle, and notes lists
def clues():
    """
    clues that will be shown at the top of the screen each scene
    """
    print(Fore.GREEN + f"\nInventory : {inventory}\n")
    print(Fore.YELLOW + f"\nRiddle: {riddle}\n")
    print(Fore.CYAN + f"\nNotes: {notes}\n")
    print("---"*60)
    print("\n")


# Main Menu / Start screen function
def main_menu():
    """
    main menu screen with 3 options to choose from
    """
    while True:
        print(Fore.RED + """
++--------------------------------------------------------++
||                                                        ||
||                                                        ||
||   ██░ ██  ▄▄▄       ██▓     ██▓     ▒█████   █     █░  ||
||  ▓██░ ██▒▒████▄    ▓██▒    ▓██▒    ▒██▒  ██▒▓█░ █ ░█░  ||
||  ▒██▀▀██░▒██  ▀█▄  ▒██░    ▒██░    ▒██░  ██▒▒█░ █ ░█   ||
||  ░▓█ ░██ ░██▄▄▄▄██ ▒██░    ▒██░    ▒██   ██░░█░ █ ░█   ||
||  ░▓█▒░██▓ ▓█   ▓██▒░██████▒░██████▒░ ████▓▒░░░██▒██▓   ||
||   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▓░▒ ▒    ||
||   ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░  ░ ▒ ▒░   ▒ ░ ░    ||
||   ░  ░░ ░  ░   ▒     ░ ░     ░ ░   ░ ░ ░ ▒    ░   ░    ||
||   ░  ░  ░      ░  ░    ░  ░    ░  ░    ░ ░      ░      ||
||                                                        ||
||   ██░ ██  ▄▄▄       ██▓     ██▓      ██████            ||
||  ▓██░ ██▒▒████▄    ▓██▒    ▓██▒    ▒██    ▒            ||
||  ▒██▀▀██░▒██  ▀█▄  ▒██░    ▒██░    ░ ▓██▄              ||
||  ░▓█ ░██ ░██▄▄▄▄██ ▒██░    ▒██░      ▒   ██▒           ||
||  ░▓█▒░██▓ ▓█   ▓██▒░██████▒░██████▒▒██████▒▒           ||
||   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░           ||
||   ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░░ ░▒  ░ ░           ||
||   ░  ░░ ░  ░   ▒     ░ ░     ░ ░   ░  ░  ░             ||
||   ░  ░  ░      ░  ░    ░  ░    ░  ░      ░             ||
||                                                        ||
||                                                        ||
||                                                        ||
++--------------------------------------------------------++
\n
""")
        print(Style.BRIGHT + Fore.GREEN +
              "Hello, Welcome to Hollow Halls Murder "
              "Mystery Game. \n")
        start = input(
            "Type 1: - Start Game\n"
            "Type 2: - View Instuctions\n"
            "Type 3: - Quit \n"
            "\n"
            ).lower()
        if start == "1":
            start_game()
            break
        elif start == "2":
            instructions()
            break
        elif start == "3":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input -\n"
                  "You must enter 1 to start the game "
                  "or 2 to view instuctions\n")
            time.sleep(3)


# Start Game Function
def start_game():
    """
    Beginning of the game function - intro message to set the scene
    """
    clear_screen()
    name = input("Please enter your Surname: \n").capitalize()
    clear_screen()

    while True:
        clues()
        print(Style.BRIGHT + "Date: 6th of March - Friday\n"
              "\n"
              f"Hello Detective.{name}, \n"
              "Welcome to Hollow Halls Private Psychiatric Facility.\n"
              "\n"
              "I see you have arrived a lot earlier then expected, \n"
              "I was just out for a run, \n"
              "please ignore the sweat and heavy breathing haha.\n"
              "\n"
              "My name is Dr.Mengele.\n"
              "I am head Psychiatist and Owner of this facility \n"
              "at Hollow Halls, \n"
              "for over 40 years.\n"
              "We house patients under the age of 40 here\n."
              "Thank you for coming on such short notice, \n"
              "we are happy to have you here.\n"
              "\n"
              "Horrible murder today, \n"
              "the body's face is completely smashed.\n"
              "It would be impossible to ID the person. \n"
              "It happened around 1:55pm \n"
              "\n"
              "Although, "
              "one of our patients is not present in their room, \n"
              "we have identified that it must be Mr.Hardy.\n"
              "He was a lovely person, \n"
              "and we are all deeply saddened and shocked \n"
              "by this incident today.\n"
              "We have reached out to his family today, \n"
              "to tell them the news.\n"
              "They never visited him.\n"
              "The body is in the main hall, \n"
              "we did not want to move it incase it gives you any clues.\n"
              "\n"
              "I know you just got here but, \n"
              "this is very important information.\n"
              "I need to share it with you right away.\n"
              "I saw four suspects running away from the body, \n"
              "down towards the testing facillaties.\n"
              "I chased them down to see their faces, \n"
              "they ran into the testing laboratory rooms.\n"
              "They were either trying to hide or run away I am not sure, \n"
              "but When they went into the testing rooms, \n"
              "I shut the doors behind them, \n"
              "I guess they did not know that it is a one way door system.\n"
              "They can not come back out.\n"
              "All four suspects are locked in their for you.\n"
              "The only problem is ... \n"
              "I do not run the testing labs I am never down here.\n"
              "Dr.Robertson does, \n"
              "you need a special Key Card to open the doors, \n"
              "which only he has. \n"
              "\n"
              "Now, "
              "unfortunatly Dr.Robertson is away on Holiday for the \n"
              "past week, "
              "but he is back tomorrow.\n"
              "This will give you a lot of time \n"
              "to be able to put the pieces together, \n"
              "and hopefully solve this brutal Murder.\n"
              "You are free to move around Hallow Halls as much as you like \n"
              "to gather evidence, \n"
              "and come to your conclusion of WHO MURDERED MR.HARDY.\n"
              )

        decision = input(Fore.BLUE + Style.BRIGHT +
                         "\n"
                         "Ok, time to explore this facility \n"
                         "and see what I can find.\n"
                         "Do you want to go to the Main hall / \n"
                         "the Living Room or the Testing Labs? \n"
                         "(Type main hall or living room or testing labs) \n"
                         ).lower()

        if decision == "main hall":
            main_hall()
            break
        elif decision == "living room":
            living_room()
            break
        elif decision == "testing labs":
            testing_labs()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "\n"
                  "Invalid input - \n"
                  "You must choose between the main hall \n"
                  "or the living room or testing labs.\n"
                  "(Type main hall or living room or testing labs into \n"
                  "terminal)\n"
                  )
            time.sleep(3)


# Common Room function
def common_room():
    """
    Common room area - when you reach a dead end you always come back
    to the common room - the main start area for the game
    """
    clear_screen()

    while True:
        clues()
        decision = input(Fore.BLUE + Style.BRIGHT +
                         "\n"
                         "You made your way back to the Common Room. \n"
                         "Would you like to go to the Living room / \n"
                         "the Main hall / the Testing Labs? \n"
                         "(Type Main Hall or Living Room or Testing Labs)\n"
                         ).lower()

        if decision == "main hall":
            main_hall()
            break
        elif decision == "living room":
            living_room()
            break
        elif decision == "testing labs":
            testing_labs()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input - \n"
                  "You must choose between the main hall or the living room \n"
                  "or testing labs.\n"
                  "(Type main hall or living room or \n"
                  "testing labs into terminal) \n"
                  )
            time.sleep(3)


# Instructions function
def instructions():
    """
    Instructions for the game
    """
    clear_screen()

    while True:
        print(
              "- At the end of each scene, you will have the choice to\n"
              "type where you would like to go next into the terminal. \n"
              "You will be given two or three choices, Type whichever \n"
              "room you\n"
              " would like to visit next. \n"
              "\n"
              "- If you enter an invalid option you will get a prompt\n "
              "that is red, saying invalid input. Wait 3 seconds, \n"
              "the scene \n"
              "will refresh and you can type in the correct input\n"
              "\n"
              "- You need to collect all 8 items to decide who you \n"
              "believe \n"
              "is the murderer. You will be told if you are correct or \n"
              "wrong.\n"
              "If you are wrong, you have to restart the game.\n"
              "\n"
              "- Along your journey you will be given plenty of clues \n"
              "so keep an eye on everything that is said.\n"
              "\n"
              "- At the top of your screens you will have your \n"
              "inventory bar, \n"
              "your riddle bar (You will need to solve a riddle) \n"
              "and your clues bar. These will be updated when you \n"
              "aqquire them.\n"
              "\n"
              "- If at any point you want to quit the game just type \n"
              "'quit' \n"
              "in to the terminal.\n"
              "\n"
              "I recommend playing some Detective music in the background\n"
              "\n"
              )
        decision = input(Fore.BLUE + Style.BRIGHT +
                         "\nType start game to start the game\n").lower()
        if decision == "start game":
            start_game()
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "invalid input - \nType start game\n")
            time.sleep(3)


# Main hall function
def main_hall():
    """
    Main hall area - choice to go look at the body or go up to the bedroom
    """
    clear_screen()

    while True:
        clues()
        print(Style.BRIGHT + "You have arrived in the main hall and see the "
              "body... \n"
              "hmm... \n"
              "The body is at the bottom of the stairs..\n"
              "It looks like somebody may have pushed the victim \n"
              "down the stairs?\n"
              "Mabye I should take a closer look\n"
              "at the body to see if I can find any clues \n"
              )

        decision = input(Fore.BLUE + Style.BRIGHT +
                         "Should I search the body \n"
                         "or make my way up to the bedrooms upstairs?\n"
                         "(Type 'body' or 'bedroom')\n"
                         ).lower()

        if decision == "body":
            clear_screen()
            if "Grey hair, Glasses, Tube" not in inventory:
                inventory.append("Grey hair, Glasses, Tube")
            if """
            Note about the body:
            Looks like mabye the killer was trying to frame someone,
            by placing the body at the end of the stairs?""" not in notes:
                notes.append("Note about the body: Looks like the "
                             "killer was trying to frame someone, "
                             "by placing the body at the end of the stairs?"
                             )
            clues()
            print(Style.BRIGHT + "\n"
                  "You make your way over to the body to take a closer look.\n"
                  "\n"
                  "Oh wow... This body was not pushed down the stairs, \n"
                  "rather it WAS STABBED to death. \n"
                  "There is multiple stab wounds in the victims back.\n"
                  "\n"
                  "Hmm.... interesting,\n"
                  "it looks like the murderer was trying to mabye frame \n"
                  "someone?\n"
                  " by placing the body at the end of the stairs?\n"
                  "Not a bad idea... \n"
                  "Who would want us too think that the body\n"
                  "had been pushed down the stairs to its death?\n"
                  "\n"
                  "Lets take a look in the victims pockets for any clues,\n "
                  "looks like a pair of old glasses and a testing tube?\n"
                  "His clothes seem ripped too.\n"
                  "I'm going to keep these items in my bag for now.\n"
                  "Oh look one last piece of his grey hair, \n"
                  "actually it looks like he was bald from what I can \n"
                  "make out.\n"
                  "Mabye I should go upstairs and look around the bedrooms!\n"
                  )

            while True:
                decision2 = input(Fore.BLUE + Style.BRIGHT +
                                  "Would you like to make your way to \n"
                                  "the bedrooms upstairs, \n"
                                  "or back to the common room? \n"
                                  "(Type 'bedroom' or 'common room') \n"
                                  ).lower()

                if decision2 == "bedroom":
                    bedroom()
                    break
                elif decision2 == "common room":
                    common_room()
                    break
                elif decision2 == "quit":
                    quit()
                else:
                    clear_screen()
                    print(Fore.RED + "Invalid input - \n"
                          "please type 'bedroom' or 'common room'"
                          "into the terminal\n")
                    time.sleep(3)
                    clues()

        elif decision == "bedroom":
            bedroom()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "\n"
                  "Invalid input -"
                  "please type 'body' or 'bedroom' into the terminal")
            time.sleep(3)


# Living room function
def living_room():
    """
    Living room function. Here you talk to Mr.Mengels wife and
    can ask her about the suspects or go to Dr.Robertsons room.
    """
    clear_screen()

    while True:
        clues()
        print(Style.BRIGHT + "You make your way to the living room and see \n"
              "Dr.Mengeles wife.\n"
              "\n"
              "You: 'Hello Ms.Mengele, I am the detetive you called. \n"
              "It is a pleasure to meet you.'\n"
              "\n"
              "Ms.Mengele: 'Hello Detective, \n"
              "It was not actually me you called it was our maid, \n"
              "I sent her home as she was in a lot of shock.\n"
              "\n"
              "You are very welcome here \n"
              "at the wealthiest Pyschiatric Facility in Europe.\n"
              "Please do ask any questions you may have about the suspects.\n"
              "I do hope Dr.Robertson arrives back tomorrow, \n"
              "so you can put away the murderer, \n"
              "bring peace back to Hallow Halls and to Mr.Hardys family.\n'"
              )
        decision = input(Fore.BLUE + Style.BRIGHT +
                         "\n"
                         "Do you want to ask Ms.Mengele about the suspects, \n"
                         "or go to Dr.Robertson's Room?\n"
                         "(Type suspects or Dr.Robertson) \n"
                         ).lower()

        if decision == "suspects":
            clear_screen()
            clues()
            print(Style.BRIGHT + "You: 'So Ms.Mengele can you tell me a \n"
                  "bit about "
                  "the suspects?'\n"
                  "\n"
                  "Ms.Mengele: ' um Yes Dectetive of course.\n"
                  "Well first of all the four suspects are \n"
                  "named Tom, Alice, Nicki, and Josh.\n"
                  "All pateints here in Hollow Halls. \n"
                  "\n"
                  "Let me start with Tom, \n"
                  "Tom is one of our disbaled pateints here, he is in \n"
                  "a wheelchair, "
                  "he got paralysed from the waist down \n"
                  "when he was serving in the war.\n"
                  "He suffers from PTSD and his room is downstairs, \n"
                  "unfortunatly we have no elevators here yet.\n"
                  "\n"
                  "Then we have Alice, poor Alice.\n"
                  "I wouldnt believe everything she says \n"
                  "she can be a bit out of it most of the times, \n"
                  "if you know what I mean.\n"
                  "She has a history of drug abuse,\n "
                  "she is also best of friends with Josh \n"
                  "they never leave eachothers sides.\n"
                  "They share a bedroom down the hall.\n"
                  "She also had beef with Mr.Hardy!!\n"
                  "\n"
                  "Nicki, well suprised me the most she is quite and calm, \n"
                  "but you know detective sometimes the quite ones\n"
                  "can do the most harm, \n"
                  "she lives upstairs and has ocd everthing is \n"
                  "spotless, she is quite small though around 5ft. \n"
                  "\n"
                  "Lastly, we have Josh. Best friends with Alice. \n"
                  "Josh is mute. Josh can not speak unfortuneatly. \n"
                  "Not much else to say about that... \n'"
                  "\n"
                  "You: All interesting points there.\n"
                  "I should try and remember this conversation.\n"
                  )

            while True:
                decision2 = input(Fore.BLUE + Style.BRIGHT +
                                  "Go to Alice and Joshs room or back \n"
                                  "to common room \n"
                                  "(Type Alice and josh or common room) \n"
                                  ).lower()

                if decision2 == "alice and josh":
                    alice_josh()
                    break
                elif decision2 == "common room":
                    common_room()
                    break
                elif decision2 == "quit":
                    quit()
                else:
                    clear_screen()
                    print(Fore.RED + "Invalid input - \n"
                          "You should have typed alice and josh or \n"
                          "common room\n")
                    time.sleep(3)
                    clues()

        elif decision == "dr.robertson":
            dr_robertson()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input - \n"
                  "please type in suspects or Dr.Robertson\n")
            time.sleep(3)


# Alice and Joshs room function
def alice_josh():
    """
    Alice and Joshs room - adds straight edge society badge to inventory.
    Back to the common room after.
    """
    clear_screen()
    if "straight edge society badge" not in inventory:
        inventory.append("straight edge society badge")
    if """
    - Notes about Alice and Josh's room:
    Drawing drawn at 2:15pm murder was at 1:55pm
    """ not in notes:
        notes.append("- Notes about Alice and Josh's room: "
                     "Drawing drawn at 2:15pm murder was at 1:55pm"
                     )

    while True:
        clues()
        print(Style.BRIGHT + "You make your way to Alices and Josh's shared \n"
              "room. \n"
              "You Look at Josh's side first.\n"
              "\n"
              "Everything looks normal, \n"
              "Josh seems to like his comics, \n"
              "he has a lot of them, \n"
              "nothing out of the ordinary. \n"
              "Oh wow amazing, he has drawn the avengers superheros, \n"
              "he is very talented.\n"
              "Drawn at 2:15pm is says on todays date...\n"
              "but Dr.Mengele said the murder was at 1:55pm \n"
              "and that they ran straight down to the testing labs?\n"
              "\n"
              "You make your way over to Alices side.\n"
              "A straight edge society badge.\n"
              "Hmm, that is conflicting from what I have heard. \n"
              )
        decision = input(Fore.BLUE + Style.BRIGHT +
                         "Let's go back to the common room to re-asses \n"
                         "(Type common room) \n"
                         ).lower()

        if decision == "common room":
            common_room()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid Input - \n "
                  "(Type Common Room)"
                  )
            time.sleep(3)


# Dr.Robertson's Room Function
def dr_robertson():
    """
    Dr.Robertsons room. Find riddle here to open safe. Piano is the answer
    Can go to the testing labs or common room from here.
    """
    clear_screen()

    if """
    I am a box who holds keys but not locks.
    With the right combination, I may unlock your soul. What am I?
    """ not in riddle:
        riddle.append("I am a box who holds keys but not locks. "
                      "With the right combination, I may unlock your soul. "
                      "What am I?"
                      )

    while True:
        clues()
        print(Style.BRIGHT + "You make your way into Dr.Robertson's Room.\n"
              "\n"
              "It is a very safisticated looking room, \n"
              "nice and tidy. Lots of graphs on the walls, \n"
              "he must live and breathe his work. \n"
              "No posters or pictures of anything, \n"
              "just an unopened box of contact lenses.\n"
              "I hope he is enjoying his Holiday Break, \n"
              "it looks like he needs it.\n"
              "\n"
              "As you search his room for clues \n"
              "you come across a piece of laminated paper \n"
              "in one of his wardrobes.\n"
              "It has a picture of a safe on it and a testing tube.\n"
              "Looks to be some sort of riddle on it, \n"
              "I wonder does this riddle lead to anything?\n "
              "I will keep it with me just incase.\n"
              "\n"
              "'I am a box who holds keys but not locks.\n"
              "With the right combination, I may unlock your soul.\n"
              "What am I?' \n"
              )
        decision = input(Fore.BLUE + Style.BRIGHT +
                         "Mabye I should go to the testing labs, \n"
                         "mabye there is something there that this \n"
                         "riddle can solve?\n"
                         "(Type Testing labs or common room)\n"
                         ).lower()

        if decision == "testing labs":
            testing_labs()
            break
        elif decision == "common room":
            common_room()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input - \n"
                  "Please type testing labs or common room\n")
            time.sleep(3)


# Testing Labs function
def testing_labs():
    """
    Testing labs area - here you can open the safe grab Dr.Robertsons
    discovery and keycard and decide to
    go into the suspects room. more clues in this room!
    """
    clear_screen()
    if "Ripped piece of clothing, " not in inventory:
        inventory.append("Ripped piece of clothing, ")

    while True:
        clues()
        print(Style.BRIGHT + "You make your way down into the testing labs.\n"
              "It looks dark and lonely down here.\n"
              "I guess not a lot of people come down here bar Dr.Robertson.\n"
              "On the ground in front of you, \n"
              "you see some fabric of clothing on the floor, \n"
              "looks like it has been ripped off? \n"
              "Hmm could be nothing...\n"
              "\n"
              "In the corner of your eye \n"
              "you see what looks like some sort of safe.\n"
              "Mabye there is something important in there? \n"
              "\n"
              "To your right you see the doors \n"
              "in which the suspects are locked in.\n"
              "you need that special key Dr.Robertson has\n"
              )

        decision = input(Fore.BLUE + Style.BRIGHT +
                         "\nDo you want to look at the safe or go "
                         "to the suspects?\n"
                         "(Type Safe or Suspects room)\n"
                         ).lower()

        if decision == "safe":
            clear_screen()
            clues()
            print(Style.BRIGHT + "You make your way over to the safe.\n"
                  "This looks tricky... it looks like I need to type in \n"
                  "a word.\n")

            while True:
                decision2 = input(Fore.BLUE + Style.BRIGHT +
                                  "\nInput the word you think is needed to \n"
                                  "open the safe!!\n"
                                  ).lower()

                if decision2 == "piano":
                    clear_screen()
                    clues()
                    print(Style.BRIGHT + "\nLooks like a diary, lets take a "
                          "look.\n"
                          "'Date march 5th 2024.\n"
                          "Time of day: 7pm.\n"
                          "\n"
                          "Today marks the most important day in my life, \n"
                          "in fact mabye one of the most important days \n"
                          "in human "
                          "history.\n"
                          "After years and years of research \n"
                          "I have figured out how to stop mental illness.\n"
                          "I have found the cure.\n"
                          "\n"
                          "No more will people be plaughed by this horrible \n"
                          "illness.\n"
                          "\n"
                          "No more will facilities and big pharma, take \n"
                          "everyones "
                          "money.\n"
                          "Tomorrow I put an end to millions of peoples \n"
                          "suffering, "
                          "I know I might get some back lash from people \n"
                          "who profit from mental illness, \n"
                          "but I hope they can see the bigger picture \n"
                          "and realize that this is what is best for the \n"
                          "world.\n"
                          "I am excited to tell the world tomorrow. \n"
                          )

                    if """
                    Dr.Robertson's Discovery,
                    Spare Key card""" not in inventory:
                        inventory.append("Dr.Robertson's Discovery, "
                                         "Spare Key card")

                    while True:
                        decision3 = input(Fore.BLUE + Style.BRIGHT +
                                          "\nWOW THIS IS VERY "
                                          "IMPORTANT -\n"
                                          "Lots of clues in that diary.\n"
                                          "hmm ... \n"
                                          "some things just dont quite add "
                                          "up...\n"
                                          "\n"
                                          "Time to make my way back to the "
                                          "common room.\n"
                                          "I need to put all my clues "
                                          "together.\n"
                                          "\n"
                                          "I think I know what happened here "
                                          "at Hallow Hall, "
                                          "after I come to a conclusion "
                                          "lets go see the suspects.\n"
                                          "Type (common room)\n"
                                          ).lower()

                        if decision3 == "common room":
                            common_room()
                            break
                        elif decision3 == "quit":
                            quit()
                        else:
                            clear_screen()
                        print(Fore.RED + "\nInvalid input -\n"
                              "Type common room\n")
                        time.sleep(3)
                        clues()
                elif decision2 == "quit":
                    quit()
                else:

                    while True:
                        print(Style.BRIGHT + "Damn, "
                              "looks like I got it wrong, \n"
                              "mabye I can find a clue for this somewhere\n"
                              )
                        wrong = input(Fore.BLUE + Style.BRIGHT +
                                      "\nType common room to go back "
                                      "and search for more clues\n"
                                      ).lower()

                        if wrong == "common room":
                            common_room()
                            break
                        elif wrong == "quit":
                            quit()
                        else:
                            clear_screen()
                            print(Fore.RED + "\nInvalid input - \n"
                                  "Type common room\n"
                                  )
                            time.sleep(3)
                            clues()

        elif decision == "suspects room":
            suspects()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input - \n"
                  "Please type safe or suspects room\n"
                  )
            time.sleep(3)


# Suspects Room Function
def suspects():
    """
    Suspects room this is the final stage of the game.
    you need all items to get into this room.
    Here you choose who the murderer was!
    """
    clear_screen()

    while True:
        clues()
        if len(inventory) < 5:
            print(Style.BRIGHT + "I do not think I have searched Hallow Halls "
                  "enough yet,\n"
                  " lets come back later when we have more clues found \n"
                  "(You Need all 8 items to enter) \n")
            decision = input(Fore.BLUE + Style.BRIGHT +
                             "\nType common room "
                             "to continue search for clues\n"
                             ).lower()

            if decision == "common room":
                common_room()
                break
            elif decision == "quit":
                quit()
            else:
                clear_screen()
                print(Fore.RED + "Invalid input - Type common room")
                time.sleep(3)
                clues()
        else:
            print(Style.BRIGHT + "You bring Mr.Mengele down to the \n"
                  "suspects room.\n"
                  "You:'So Mr.Mengele I have some great news, \n"
                  "I found Dr.Robertsons special keycard \n"
                  "to open the doors.\n"
                  "Let's get this over with right now, \n"
                  "'I know who the killer is.\n'"
                  "\n"
                  "Dr.Mengele: 'Oh are you sure? \n"
                  "are you positive you dont want to wait the night \n"
                  "and sleep on it?'\n"
                  "\n"
                  "You: 'No I am 100% positive on who the killer is \n"
                  "- before we go in their let me explain my reasoning \n"
                  "to you...'\n"
                  "\n"
                  "After explaining everything to Dr.Mengele. \n"
                  "You make your way into the suspects room.\n"
                  "All four suspects look heavily sedated and dazed... \n"
                  "as expected... \n"
                  )
            decision2 = input(Fore.BLUE + Style.BRIGHT +
                              "\nIt is time for you to choose "
                              "WHO WAS THE MURDERER??!!\n"
                              ).lower()

            if decision2 == "dr.mengele":
                winner()
            else:
                loser()


def winner():
    clear_screen()
    print(Style.BRIGHT + "IT WAS YOU DR.MENGELE !! \n"
          "\n"
          "You might be asking how did I figure it out? Well let me \n"
          "explain "
          ".....\n"
          "\n"
          "First of all, You said you were out for a 'run', \n"
          "you were sweating, and out of breathe.\n"
          "You were shocked by my early arrival, "
          "the only reason you were sweating was because you were in a \n"
          "rush to "
          "cover up this murder after you heard the maid call me.\n"
          "When you were told I arrived earlier then expected you were \n"
          "shocked "
          "and ran around as quickly as possible to try and cover \n"
          "this all up"
          "but you failed.\n"
          "This was the first lie of many. \n"
          "In fact you were running around trying to frame these four \n"
          "'suspects' "
          "which you had locked\n"
          "in the basement because they saw you murderer this victim.\n"
          "\n"
          "Forty years here huh? You are quite old.. \n"
          "Nice set of grey hair you have Dr. \n"
          "Almost as if the only piece of hair on the victims \n"
          "body was infact grey,"
          "and none of your 'suspects' have grey hair? \n"
          "You mentioned you did not go near or move the body? \n"
          "How would the grey hair get there then? The victim \n"
          "was aslso bald.\n"
          "\n"
          "Now... you trapped them 'suspects' in there Dr, \n"
          "they did not run in there themselves. \n"
          "You drugged them after you saw them see you murder this victim.\n"
          "As you can tell by how drugged up they all look right now \n"
          "you used "
          "some sort of amnesia drug so that they would forget \n"
          "about all this in the morning.\n"
          "You had a keycard this whole time because your one is \n"
          "the exact same "
          "one I found to unlock this door.\n"
          "You had them trapped in here because you knew they "
          "could not escape \n"
          "from the inside. \n"
          "But this whole time you were just lying to me about not \n"
          "being able to open the door, \n"
          "and that only Dr.Robertson had a special keycard. \n"
          "You are the owner for christ sake of course you have a keycard. \n"
          "You wanted me to stay the night, \n"
          "so that you could come up with a plan on what to do with these \n"
          "four 'suspects' during the night ... \n"
          "mabye you were going to kill them all and stage an 'escape'?? \n"
          "You needed them trapped so you could frame them one way or \n"
          "another and you needed time to think and come up with a plan\n "
          "as I got here very quickly.\n"
          "\n"
          "I must say you done a fairly good job in trying to \n"
          "frame these suspects "
          "but you missed some key details which let me to this discovery \n"
          "that it was you and not them.\n"
          "\n"
          "You moved the body to the bottom of the stairs, \n"
          "this is where the grey hair came from. \n"
          "You then tried to frame Tom. \n"
          "You knew you had stabbed the victim in the back.\n"
          "You knew I would see the stab wounds and you thought \n"
          "I would think that Tom was actually the one doing the framing. \n"
          "You thought I would think that Tom placed the body, \n"
          "at the bottom of the stiars, so that it looked like someone \n"
          "pushed "
          "the body to the stairs to his death. \n"
          "Of course Tom can not walk up the stairs and you used \n"
          "his disability "
          "as a chance for me to think he was the one doing the framing. \n"
          "When in fact is was all you. \n"
          "Now of course it still could have been Tom.. \n"
          "but ...It was not Tom because the actual murder weapon "
          "was upstairs !! \n"
          "There would have been no way Tom could have stashed the \n"
          "Murder weapon "
          "up there. So that rules him out.\n"
          "\n"
          "Now you ask what about Nicki? \n"
          "Nicki has OCD which your wife told me. \n"
          "Everything in Nickis rooms is super clean. \n"
          "I found blood droplets in the sink.. \n"
          "How would she has missed this?\n"
          "Ah yes, because it was not her... \n"
          "it was you in a rush trying to clean the blood from the knife, \n"
          "you left some droplets in the sink because you were \n"
          "in such a rush.\n"
          "You then tried to 'hide' the knife. But really you wanted \n"
          "me to see it, \n"
          "you wanted me to mabye think it was Nicki who murdered the \n"
          "victim.\n"
          "but again DR. \n"
          "you made a mistake. \n"
          "It could not have been Nicki because you placed it in a \n"
          "really high place, Nicki could never reach that she is only 5ft. \n"
          "\n"
          "Your wife is not much better. \n"
          "She was filling me with some lies too... \n"
          "She was trying to set up Alice telling me she was a bad \n"
          "drug user \n"
          "and that she could get crazy.\n"
          "She also said she had 'beef' with Mr.Hardy the alledged victim. \n"
          "Now I am not sure if she had beef with Mr.Hardy but I do not \n"
          "care \n"
          "but Alice was not a drug user inface Alice was the opposite \n"
          "- Alice was part of the straight edge society which means \n"
          "she never "
          "done hardcore drugs in her life.\n"
          "\n"
          "Josh and Alice were also togehter after the murder Josh \n"
          "was drawing "
          "a pciture of his favourite comic book heros this would have \n"
          "taken hours.\n"
          "Josh and Alice sign the back of every single picture Josh \n"
          "drew with "
          "a date and time of completion.\n"
          "There is no way they could have commited this murder because \n"
          "they were in there rooms at the time. You said the 'suspects' \n"
          "ran to the testing labs.\n"
          "This is not true they must have heard the maids screem of seeing \n"
          "the body in the main hall and you saw them looking out of there \n"
          "rooms "
          "and drugged them and brought them down.\n"
          "\n"
          "So it was not Tom, Nicki, Alice, or Josh. IT WAS YOU ! \n"
          "\n"
          "Now.... back to explaining why I did not care that Alice may \n"
          "or may "
          "not have had beef with Mr.Hardy... Mr.hardy has not been on your \n"
          "records for months.. \n"
          "I presume you may have killed him too... \n"
          "as he is no where to be found for months from your records \n"
          "and his family never visits him.\n"
          "He is an easy pateint to pretend that this is his body, \n"
          "no one would question it, not even the family. \n"
          "\n"
          "That body IS NOT MR.HARDY'S BODY! THAT BODY IS \n"
          "DR.ROBERTSON'S BODY!!\n"
          "\n"
          "You killed Dr.Robertson because of what he had discovered! \n"
          "You knew it would destroy your wealth!! \n"
          "He was about to save millions of lives and you murdered him in \n"
          "cold blood because of how selfish you are.\n"
          "You are a sick man Dr.Mengele - \n"
          "Luckiliy I have figured it out and I will get Dr.Robertsons \n"
          "work in the hands of the right people.\n"
          "\n"
          "You destroyed Dr.Robertsons face because you did not want \n"
          "him ID'd "
          "- You were going to dispose of his body during the night. \n"
          "You used an excuse that he was on Holiday. \n"
          "You were going to use that as an excuse as \n"
          "to why he never returned.... \n"
          "and must have died over there.\n"
          "I read his diary. He was here YESTERDAY  Dr.... \n"
          "You told me he has been gone for a week on Holiday... \n"
          "\n"
          "There was some piece of ripped clothing down here I found near \n"
          "the testing labs... It was his.\n"
          "You stabbed him down here after he told you about the discovery \n"
          "he made. You could not let this happen. \n"
          "You stabbed him and a piece of his clothing came off with it, \n"
          "his body when I searched it in the main hall \n"
          "has a peice of clothing "
          "missing from his back.\n"
          "You moved him up to the main hall, \n"
          "the maid saw the body and called me. \n"
          "You then had to quickly come up with a solution to frame "
          "someone else and get any\n"
          "suspicion away from you.\n"
          "He also had a pair of glasses and a testing tube in his pocket. \n"
          "You really should have taken them out Dr.Mengele... \n"
          "but I know you were in a rush.\n"
          "Interesting how Dr.Robertson had some unopened contact \n"
          "lenses in his "
          "room. \n He must still stick to wearing his glasses... \n"
          "The testing tube is a bit of a giveaway I dont think I need to \n"
          "explain that.\n"
          "\n"
          "So there we have it... YOU MURDERED DR.ROBERTSON. \n"
          "\n"
          "'You have the right to remain silent. \n"
          "Anything you say can and will be used against you in a \n"
          "court of law. \n"
          "You have the right to an attorney. \n"
          "If you cannot afford an attorney, one will be provided for you. \n"
          "Do you understand the rights I have just read to you?'\n "
          "\n"
          "........................................................."
          "......... \n"
          "\n"
          )
    print(Fore.GREEN + "CONGRATULATIONS YOU HAVE SOLVED "
          "THE HALLOW HALLS MURDER\nMYSTERY "
          "WELL DONE !! \n"
          "\n"
          "GAME OVER. \n")

    while True:
        ending = input(Fore.BLUE + Style.BRIGHT +
                       "Type quit to quit the game \n"
                       )
        if ending == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input -\n Type quit"
                  )
            time.sleep(3)


def loser():
    clear_screen()

    while True:
        print(Style.BRIGHT + "Damn you got it wrong...\n"
              "try again next time... \n"
              "YOU JUST SENT AN INNOCENT PERSON TO PRISON HOW COULD YOU!!\n"
              )
        ending = input(Fore.BLUE + Style.BRIGHT +
                       "Type restart to restart the game\n"
                       ).lower()

        if ending == "restart":
            clear_screen()
            main_menu()
            break
        elif ending == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input - \n Type Restart\n"
                  )
            time.sleep(3)


# Bedroom
def bedroom():
    """
    Bedroom fucntion - can go to the bathroom and from there the common room
    Finds knife and some more clues in this scene. Adds Knife to inventory.
    and some notes about the room.
    """
    clear_screen()
    if "Knife" not in inventory:
        inventory.append("Knife")

    while True:
        clues()
        print(Style.BRIGHT + "You make your way up the stairs and search \n"
              "the bedrooms.\n"
              "\n"
              "You dont seem to see anything suspicious \n"
              "until finally the last room.\n"
              "\n"
              "In the last room as you are looking, \n"
              "you see something shiny at the very top of the wardrobe, \n"
              "stashed away in the far corner.\n"
              "You check and you find a knife - AH HA!! \n"
              "This must be the murder weapon, \n"
              "but the knife looks very clean and has no blood on it??\n"
              "\n"
              "Let's keep this with us.\n"
              "The murderer must be very tall to reach up there.\n"
              )

        decision = input(Fore.BLUE + Style.BRIGHT +
                         "\nThe bathroom door seems to be open \n"
                         "in this bedroom, "
                         "Do you want to have a look in there 2 \n"
                         "or do you want to make your way "
                         "back to the common room?\n"
                         "Type (Bathroom / Common Room) \n"
                         ).lower()

        if decision == "bathroom":
            clear_screen()
            clues()

            if """
            - Notes about the bathroom/bedroom:
            - Drops of Blood in sink
            - Killer in a rush
            - Who's Bedroom is that? Must be very tall""" not in notes:
                notes.append("- Notes about the bathroom/bedroom: "
                             ", Drops of Blood in sink, "
                             "Killer in a rush, Who's Bedroom is that?, "
                             "Must be very tall")
            print(Style.BRIGHT + "Medicine cabnit looks empty, nice and \n"
                  "clean... \n"
                  "\n"
                  "what is that?\n"
                  "\n"
                  "Oh wow, \n"
                  "uhh jesus there looks like there is some drops of blood \n"
                  "in the sink..\n"
                  "This may be where the killer sleeps this may be \n"
                  "the killer..\n"
                  "It looks like they were in a \n"
                  "rush and did not clean properly. \n"
                  "\n"
                  "Ok lets make my way back downstairs \n"
                  "and into the common room to re-asses. \n"
                  )

            while True:
                home = input(Fore.BLUE + Style.BRIGHT +
                             "\nTime to make my way back "
                             "to the Common Room \n"
                             "(Type Common Room to get there) \n"
                             ).lower()

                if home == "common room":
                    common_room()
                    break
                elif home == "quit":
                    quit()
                else:
                    clear_screen()
                    print(Fore.RED + "Invalid input -\n"
                          "please type in common room to the terminal\n"
                          )
                    time.sleep(3)
                    clues()

        elif decision == "common room":
            common_room()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print(Fore.RED + "Invalid input -\n"
                  "please type in Bathroom or Common Room to the terminal \n"
                  )
            time.sleep(3)


# Calling Functions
clear_screen()
main_menu()
