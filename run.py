# Your code goes here.


inventory = []

def main_menu():
    print("Hello, Welcome to Hollow Halls Murder Mystery Game. \n")
    start = input("Input 1: - Start Game \nInput 2: - View Instuctions").lower()
    if start == "1":
        start_game()
    elif start == "2":
        instructions()
    else: 
        print("Invalid input - You must enter 1 to start the game or 2 to view instuctions")

def start_game():
    print("starting game")



def instructions():
    print("instructions")

main_menu()



