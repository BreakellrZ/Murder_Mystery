# Inventory for items picked up in the game
inventory = []

# Inventory for riddle notes picked up in the game
riddle = []

# notes
notes = []

# Main Menu / Start screen function
def main_menu():
    print("Hello, Welcome to Hollow Halls Murder Mystery Game. \n")
    start = input("Input 1: - Start Game \nInput 2: - View Instuctions: \n").lower()
    if start == "1":
        start_game()
    elif start == "2":
        instructions()
    else: 
        print("Invalid input - You must enter 1 to start the game or 2 to view instuctions")

# Start Game Function 
def start_game():
    name = input("Please enter your Surname: ").capitalize()
    print(f"Hello Detective.{name}. Welcome to Hollow Halls Private Psychiatric Facility. I see you have arrived earlier then expected, I was just out for a run, please ignore the sweat and heavy breathing haha, I was just about to hop in to the shower. My name is Dr.Mengele, I am head Psychiatist here at Hollow Halls for over 40 years. Thank you for coming, we are happy to have you here. My wife Lauren found the body, full of blood in the main hall just under the stairs. It is a horrible site to see, she is in shock from it, the poor thing, as am I. Lauren said she saw four suspects running away from the scene, she ran after them and saw the suspects make their way down to the cellar and into the testing labs. By the looks of it they were trying to hide or escape the scene and found themselves locked in the room. The suspects triggered the defense alarm and locked the doors from the inside as they did not put in the correct code to turn of the alarm when they ran into the testing labs. I am honestly not sure what the code is to stop the alarms and re-open the doors. Dr.Robertson is away on holidays and wont be back until tomorrow he is head of the testing labs. You might have to come back Tomorrow to talk with the suspects but until then you are free too search the Facility we are in the common room currently, hopefully you find some clues and can catch the killer and arrest them when Dr.Robertson comes back.")
    
    decision1 = input("Ok, time to exlore this facility and see what I can find. \n Do you want to go to the main hall or the living room? (type main hall or living room) \n").lower()
    if decision1 == "main hall":
        main_hall()
    elif decision1 == "living room":
        living_room()
    else:
        print("Invalid input - You must choose between the main hall or the living room (Type main hall or living room into terminal)")


# Instructions function
def instructions():
    print("instructions")


# Main Hall function
def main_hall():
    print("You have arrived in the main hall and see the body... hmm... it is at the bottom of the stairs.. It looks like somebody may have pushed the victim down the stairs? I should take a closer look at the body to see if I can find any clues")
    decision2 = input("Should I search the body or make my way up to the bedrooms upstairs? \n (Type body or bedroom) \n" )
    if decision2 == "body":
        print("Oh wow.. it does not appear that the victim was pushed down the stairs, rather it looks like they have been STABBED in the back. Mabye one of the suspects is trying to frame someone else? It looks like they were trying to make it seem like the victim fell or was pushed down the stairs. Oh look a grey hair, must have been his last bit of hair on his bald head poor guy. He has a set of glasses in his pocket and a some sort of tube. I should write this down in my notes and keep these items")
        notes.append(" Note about the body: Looks like the killer was trying to frame someone by placing the body at the end of the stairs - Glasses, Grey hair and tube")
        inventory.append("Grey hair," + " " +"Glasses," + " " "Tube")
        print(f" Notes: {notes}")
        print(f"Inventory: {inventory}")
    elif decision2 == "bedroom":
        bedroom()
    else:
        print("Invalid input - please type in body or bedroom to the terminal")


#Living room
def living_room():
    print("hi")

# Bedroom
def bedroom():
    print("hi")

# Calling Functions
main_menu()



