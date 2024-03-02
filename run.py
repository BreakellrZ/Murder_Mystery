import os

# Inventory for items picked up in the game
inventory = []

# Inventory for riddle notes picked up in the game
riddle = []

# notes
notes = []

# Notes on suspects
suspects = []


# Clear the screen in a cross-platform manner
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# Main Menu / Start screen function
def main_menu():
    while True:
        print("Hello, Welcome to Hollow Halls Murder Mystery Game. \n")
        start = input("Type 1: - Start Game \n Type 2: - View Instuctions \n Type 3: - Quit \n").lower()
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
            print("Invalid input - You must enter 1 to start the game or 2 to view instuctions \n")
            
        

# Start Game Function 
def start_game():
    clear_screen()
    name = input("Please enter your Surname: ").capitalize()
    clear_screen()
    while True:
        print(f"""Hello Detective.{name}, Welcome to Hollow Halls Private Psychiatric Facility.

I see you have arrived earlier then expected, I was just out for a run,
please ignore the sweat and heavy breathing haha, I was just about to hop in to the shower.
My name is Dr.Mengele, I am head Psychiatist here at Hollow Halls for over 40 years.
Thank you for coming, we are happy to have you here.

My wife Lauren found the body, full of blood in the main hall just under the stairs.
It is a horrible site to see, she is in shock from it, the poor thing, as am I.
Lauren said she saw four suspects running away from the scene,
she ran after them and saw the suspects make their way down to the cellar and into the testing labs.
By the looks of it they were trying to hide or escape the scene and found themselves locked in the room.
The suspects triggered the defense alarm, and locked the doors from the inside,
as they did not put in the correct code to turn of the alarm when they ran into the testing labs.
I am honestly not sure what the code is to stop the alarms and re-open the doors. 
Dr.Robertson is away on holidays and wont be back until tomorrow he is head of the testing labs.

You might have to come back Tomorrow to talk with the suspects,
but until then you are free too search the Facility we are in the common room currently,
hopefully you find some clues and can catch the killer and arrest them when Dr.Robertson comes back.
""")
        decision = input("""\nOk, time to exlore this facility and see what I can find.\n
Do you want to go to the main hall or the living room?
(type main hall or living room) \n""").lower()
        if decision == "main hall":
            main_hall()
            break
        elif decision == "living room":
            living_room()
            break
        elif decision == "quit": 
            quit()
        else:
            clear_screen()
            print("""Invalid input - You must choose between the main hall or the living room.\n
            (Type main hall or living room into terminal) \n""")
            

# Common Room function
def common_room():
    clear_screen()
    while True:
        decision = input("""You made your way back to the Common Room. \n
Would you like to go to the Living room or the Main hall?
(Main Hall / Living Room) \n""").lower()
        if decision == "main hall":
            main_hall()
            break
        elif decision == "living room":
            living_room()
            break
        elif decision == "quit": 
            quit()
        else:
            clear_screen()
            print("""Invalid input - You must choose between the main hall or the living room.
(Type main hall or living room into terminal) \n""")
        

# Instructions function
def instructions():
    print("instructions")


def main_hall():
    clear_screen()
    while True:
        print("""You have arrived in the main hall and see the body...
hmm...
it is at the bottom of the stairs..
It looks like somebody may have pushed the victim down the stairs?
I should take a closer look at the body to see if I can find any clues \n""")
        decision = input("""Should I search the body or make my way up to the bedrooms upstairs?
\n(Type 'body' or 'bedroom') \n""").lower()
        if decision == "body":
            clear_screen()
            print("""Oh wow.. it does not appear that the victim was pushed down the stairs,
rather it looks like they have been STABBED in the back.
Maybe one of the suspects is trying to frame someone else?
It looks like they were trying to make it seem like the victim fell,
or was pushed down the stairs.
Oh look a grey hair, must have been his last bit of hair on his bald head poor guy.
He has a set of glasses in his pocket and some sort of tube.
I should write this down in my notes and keep these items \n""")
            notes.append("""Note about the body:Looks like the killer was trying to frame someone by placing the body at the end of the stairs.- Glasses, Grey hair, and tube""")
            inventory.append("Grey hair, Glasses, Tube")
            print(f"\nNotes: {notes}")
            print(f"\nInventory: {inventory}")
            while True:
                decision2 = input("""Would you like to make your way to the bedrooms upstairs,
or back to the common room?
\n (Type 'bedroom' or 'common room') \n """).lower()
                if decision2 == "bedroom":
                    bedroom()
                    break
                elif decision2 == "common room":
                    common_room()
                    break
                elif decision == "quit": 
                    quit()
                else: 
                    clear_screen()
                    print("Invalid input - please type 'bedroom' or 'common room' into the terminal")
        elif decision == "bedroom":
            bedroom()
            break
        elif decision == "quit": 
            quit()
        else:
            clear_screen()
            print("Invalid input - please type 'body' or 'bedroom' into the terminal")


#Living room
def living_room():
    clear_screen()
    while True:
        print("""You make your way to the living room and see Dr.Mengeles wife.
she looks like as if nothing has happened but she was startled by my arrival.
\n'Hello Ms.Mengele, I am the detetive you called. It is a pleasure to meet you.'""")
        decision = input("""Do you want to ask Ms.Mengele about the suspects,
or go to Dr.Robertson's Room?
\n(Type suspects or Dr.Robertson) \n""" ).lower()
        if decision == "suspects":
            clear_screen()
            print("""You: So Ms.Mengele can you tell me a bit about the suspects? \n
Ms.Mengele: um Yes Dectetive of course.
Well first of all the four suspects are named Tom, Alice, Nicki, and Josh.
All pateints here in Hollow Halls.

Let me start with Tom, Tom is one of our disbaled pateints here, he is in a wheelchair,
he got paralysed from the waist down when he was serving in the war. 

Then we have Alice, poor Alice. 
I wouldnt believe everything she says she can be a bit out of it most of the times,
if you know what I mean.
She has a history of drug abuse,
she is also best of friends with Josh they never leave eachothers sides,
they share a bedroom down the hall. 
            
Nicki then is what suprised me the most she is quite and calm,
but you know detective sometimes the quite ones can do the most harm.

Lastly, we have Josh. Best friends with Alice.
Josh is am ... mute. Ya, Josh can not speak unfortuneatly.
Not much else to say about that.. uh ya.

You: All interesting points there let me write them down.""")
        

            suspects.append("""--- Tom: Wheelchair bound - interesting that the murder looked like it wanted to be framed,from someone pushing someone down the stairs...Obviously Tom could not have got up the stairs. --- Alice: Alice drug addict not fully there from what Ms.Mengele said. --- Nicki: The most suprised suspect,very quiet she is only about 4ft 10 very petite,has OCD, she likes to be very clean. --- Josh: Room mates and best friend with Alice down the hall. Mute can not speak.""")
            print(f"\n Suspect notes: {suspects}")
            while True:
                decision2 = input("\nGo to Alice and Joshs room or back to common room \n")
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
                    print("Invalid input - You should have typed alice and josh or common room")
        elif decision == "dr.robertson":
            dr_robertson()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print("Invalid input please type in suspects or calm")

def alice_josh():
    clear_screen()
    while True:
        print("""\nYou make your way to Alices and Josh's shared room. You Look at Josh's side first.
    Everything looks normal, Josh seems to like his comics, he has a lot of them, nothing out of the ordinary.

    You make your way over to Alices side.
    Oh cool, a straight edge society badge. Hmm, that is conflicting from what I have heard. \n
    """)
        inventory.append("straight edge society badge")
        decision = input("\nLet's go back to the common room to re-asses (Type common room) \n").lower()
        if decision == "common room":
            common_room()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print("\n Invalid Input - type Common Room \n")

    

def dr_robertson():
    clear_screen()
    while True:
        print("""You make your way into Dr.Robertson's Room.
It is a very safisticated looking room, nice and tidy. Lots of graphs on the walls,
he must live and breathe his work. No posters or pictures of anything,
just an unopened box of contact lenses.
He must have love his job. I hope he is enjoying his Holiday Break, it looks like he needs it.

As you search his room for clues you come across a piece of laminated paper in one of his wardrobes.
It has a picture of a safe on it and a testing tube. Looks to be some sort of riddle on it,
I wonder does this riddle lead to anything? I will keep it with me just incase.

'I am a box who holds keys but not locks.
With the right combination, I may unlock your soul.
What am I? \n""")
        riddle.append("'I am a box who holds keys but not locks. With the right combination, I may unlock your soul. What am I?'")
        decision = input("""\n Mabye I should go to the testing labs,
mabye there is something there that this riddle can solve?\n 
(Type Testing labs or common room)\n""").lower()
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
            print("\ninvalid input, Please type testing labs or common room\n")
        
        
def testing_labs():
    clear_screen()
    while True:
        print("""You make your way down into the testing labs. It looks dark and lonely down here.
I guess not a lot of people come down here bar Dr.Robertson.
On the ground in front of you, you see some fabric of clothing on the floor,
looks like it has been ripped off? Hmm could be nothing..

In the corner of your eye you see what looks like some sort of safe.
Mabye there is something important in there? 

To your right you see the doors in which the suspects are locked in. """)

        inventory.append("Ripped piece of clothing, ")

        decision = input("""\nDo you want to look at the safe or go to the suspects?\n
(Type Safe or Suspects)\n""").lower()

        if decision == "safe":
            clear_screen()
            print("""\nYou make your way over to the safe.
This looks tricky... it looks like I need to type in some letters or a word.\n""")
            while True:
                decision2 = input("""\nInput the word you think is needed to open the safe\n""")
                if decision2 == "piano":
                    print(""" """)
                    inventory.append("Dr.Robertson's Discovery")
                    decision3 = input("""WOW THIS IS IMPORTANT - Time to make my way back to the common room.
    I need to put all my clues together, I think I know what happened here at Hallow Hall.""")
                    while True:
                        if decision3 == "common room":
                            common_room()
                            break
                        elif decision3 == "quit":
                            quit()
                        else:
                            clear_screen()
                            print("Invalid input - Type common room")
                elif decision2 == "quit":
                    quit()
                else:
                    while True:
                        print("Damn looks like I got it wrong, mabye I can find a clue for this somewhere")
                        wrong = input("Type common room to go back and search for more clues")
                        if wrong == "common room":
                            common_room()
                            break
                        elif wrong == "quit":
                            quit()
                        else:
                            clear_screen()
                            print("invalid input - type common room")

        elif decision == "suspects":
            suspects()
            break
        else:
            clear_screen()
            print("\ninvalid input - Please type safe or common room\n")

                
            
def suspects():
    pass

# Bedroom
def bedroom():
    clear_screen()
    while True:
        print("""You make your way up the stairs and search the bedrooms.
You dont seem to see anything suspicious until finally the last room.

In the last room as you are looking through the drawers,
You find nothing, 
until you see something shiny at the very top of the wardrobe,
stashed away in the far corner.
You check and you find a knife - AH HA!!
This must be the murder weapon, but the knife looks very clean and has no blood on it??

Let's keep this with us and add it to my inventory of items
- The murderer must be very tall to reach up there.\n""")
        
        inventory.append("Knife")
        
        decision = input(""" \n The bathroom door seens to be open in this bedroom,
Do you want to have a look in there or do you want to make your way back to the common room?\n
(Bathroom / Common Room) \n""").lower()
        if decision == "bathroom":
            clear_screen()
            print("""Medicine cabnit looks empty, looks nice and clean...
what is that?

Oh wow, uhh jesus there looks like there is some drops of blood in the sink..
This must be where the killer sleeps this must be the killer..
It looks like they were in a rush and did not clean properly.

- Ok lets make my way back downstairs and into the common room to re-asses. \n""")
            notes.append(""" - Notes about the bathroom/bedroom:- Drops of Blood in sink - Killer in a rush - Who's Bedroom is that? - Sobriety medal.""")
            print(f"\nNotes: {notes}")

            while True:
                home = input("\nTime to make my way back to the Common Room (Type Common Room to get there) \n")
                if home == "common room":
                    common_room()
                    break
                elif home == "quit":
                    quit()
                else:
                    clear_screen()
                    print("Invalid input - please type in common room to the terminal\n") 

        elif decision == "common room":
            common_room()
            break
        elif decision == "quit": 
            quit()
        else:
            clear_screen()
            print("Invalid input - please type in Bathroom or Common Room to the terminal \n")
            

# Calling Functions
main_menu()



