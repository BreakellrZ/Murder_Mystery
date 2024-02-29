import os


# Inventory for items picked up in the game
inventory = []

# Inventory for riddle notes picked up in the game
riddle = []

# notes
notes = []


# Clear the screen in a cross-platform manner
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

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
    clear_screen()
    name = input("Please enter your Surname: ").capitalize()
    print(f"Hello Detective.{name}. Welcome to Hollow Halls Private Psychiatric Facility. I see you have arrived earlier then expected, I was just out for a run, please ignore the sweat and heavy breathing haha, I was just about to hop in to the shower. My name is Dr.Mengele, I am head Psychiatist here at Hollow Halls for over 40 years. Thank you for coming, we are happy to have you here. My wife Lauren found the body, full of blood in the main hall just under the stairs. It is a horrible site to see, she is in shock from it, the poor thing, as am I. Lauren said she saw four suspects running away from the scene, she ran after them and saw the suspects make their way down to the cellar and into the testing labs. By the looks of it they were trying to hide or escape the scene and found themselves locked in the room. The suspects triggered the defense alarm and locked the doors from the inside as they did not put in the correct code to turn of the alarm when they ran into the testing labs. I am honestly not sure what the code is to stop the alarms and re-open the doors. Dr.Robertson is away on holidays and wont be back until tomorrow he is head of the testing labs. You might have to come back Tomorrow to talk with the suspects but until then you are free too search the Facility we are in the common room currently, hopefully you find some clues and can catch the killer and arrest them when Dr.Robertson comes back.")
    
    decision = input("Ok, time to exlore this facility and see what I can find. \n Do you want to go to the main hall or the living room? (type main hall or living room) \n").lower()
    if decision == "main hall":
        main_hall()
    elif decision == "living room":
        living_room()
    else:
        print("Invalid input - You must choose between the main hall or the living room (Type main hall or living room into terminal)")


# Common Room function
def common_room():
    clear_screen()
    decision = input("You made your way back to the Common Room. Would you like to go to the Living room or the Main hall? (Main Hall / Living Room) \n").lower()
    if decision == "Main Hall":
        main_hall()
    elif decision == "Living Room":
        living_room()
    else:
        print("Invalid input - You must choose between the main hall or the living room (Type main hall or living room into terminal)")
    

# Instructions function
def instructions():
    print("instructions")


def main_hall():
    clear_screen()
    print("You have arrived in the main hall and see the body... hmm... it is at the bottom of the stairs.. It looks like somebody may have pushed the victim down the stairs? I should take a closer look at the body to see if I can find any clues")
    decision = input("Should I search the body or make my way up to the bedrooms upstairs? \n (Type 'body' or 'bedroom') \n").lower()
    if decision == "body":
        print("Oh wow.. it does not appear that the victim was pushed down the stairs, rather it looks like they have been STABBED in the back. Maybe one of the suspects is trying to frame someone else? It looks like they were trying to make it seem like the victim fell or was pushed down the stairs. Oh look a grey hair, must have been his last bit of hair on his bald head poor guy. He has a set of glasses in his pocket and some sort of tube. I should write this down in my notes and keep these items")
        notes.append("Note about the body: Looks like the killer was trying to frame someone by placing the body at the end of the stairs - Glasses, Grey hair, and tube")
        inventory.append("Grey hair, Glasses, Tube")
        print(f"Notes: {notes}")
        print(f"Inventory: {inventory}")
        decision2 = input("Would you like to make your way to the bedrooms upstairs or back to the common room? \n (Type 'bedroom' or 'common room') \n").lower()
        if decision2 == "bedroom":
            bedroom()
        elif decision2 == "common room":
            common_room()
        else: 
            print("Invalid input - please type 'bedroom' or 'common room' into the terminal")
    elif decision == "bedroom":
        bedroom()
    else:
        print("Invalid input - please type 'body' or 'bedroom' into the terminal")


#Living room
def living_room():
    clear_screen()
    print("hi")


# Bedroom
def bedroom():
    clear_screen()
    print("You make your way up the stairs and search the bedrooms. You dont seem to see anything suspicious until finally the last room. In the last room as you are looking through the drawers and find nothing but you see something shiny under the bed, you check and you find a knife - AH HA - this might be the murder weapon but the knife looks very clean and has no blood on it?? Let's keep this with us and add it to my inventory of items")
    inventory.append("Knife")
    decision = input("The bathroom door seens to be open in this bedroom, Do you want to have a look in there or do you want to make your way back to the common room? (Bathroom / Common Room)").lower()
    if decision == "bathroom":
        print("Medicine cabnit looks empty, looks nice and clean... uhh jesus there looks like there is some drops of blood in the sink.. this must be where the killer sleeps this must be the killer.. I must ask to see who's room this is! It looks like they were in a rush and did not clean properly - Ok lets make my way back downstairs and into the common room to re-asses.")
        notes.append(" -Notes about the bathroom/bedroom: Drops of Blood in sink - killer in a rush - Who's Bedroom is that?")
        print(notes)
        home = input("Time to make my way back to the Common Room (Type Common Room to get there) \n")
        if home == "common room":
            common_room()
        else:
            print("Invalid input - please type in common room to the terminal") 
    elif decision == "common room":
        common_room()
    else:
        print("Invalid input - please type in Bathroom or Common Room to the terminal")
         


# Calling Functions
main_menu()



