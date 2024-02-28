# Inventory for items picked up in the game
inventory = []

# Inventory for riddle notes picked up in the game
riddle_notes = []

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

    print(f"Hello Detective.{name}. Welcome to Hollow Halls Private Psychiatric Facility. I see you have arrived earlier then expected, I was just out for a run, please ignore the sweat and heavy breathing haha, I was just about to hop in to the shower. My name is Dr.Mengele, I am head Psychiatist here at Hollow Halls for over 40 years. Thank you for coming, we are happy to have you here. My wife Lauren found the body, full of blood in the main hall just under the stairs. It is a horrible site to see, she is in shock from it, the poor thing, as am I. Lauren said she saw four suspects running away from the scene, she ran after them and saw the suspects make their way down to the cellar and into the testing labs. By the looks of it they were trying to hide or escape the scene and found themselves locked in the room. The suspects triggered the defense alarm and locked the doors from the inside as they did not put in the correct code to turn of the alarm when they ran into the testing labs. I am honestly not sure what the code is to stop the alarms and re-open the doors. Dr.Robertson is away on holidays and wont be back until tomorrow he is head of the testing labs. You might have to come back Tomorrow to talk with the suspects but until then you are free too search the Facility, hopefully you find some clues and can catch the killer and arrest them when Dr.Robertson comes back.")



# Instructions function
def instructions():
    print("instructions")


# Calling Functions
main_menu()



