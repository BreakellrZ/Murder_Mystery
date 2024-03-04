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


# Clues
def clues():
        print(f"\nInventory : {inventory}\n")
        print(f"\nRiddle: {riddle}\n")
        print(f"\nNotes: {notes}\n")
        print("---"*20)
        

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
    name = input("\nPlease enter your Surname: \n").capitalize()
    clear_screen()
    while True:
        clues()
        print(f""" Date: 6th of March - Friday

Hello Detective.{name}, Welcome to Hollow Halls Private Psychiatric Facility.

I see you have arrived a lot earlier then expected, I was just out for a run,
please ignore the sweat and heavy breathing haha.
My name is Dr.Mengele. I am head Psychiatist and Owner of this facility here at Hollow Halls, for over 40 years.
We house patients under the age of 40 here.
Thank you for coming on such short notice, we are happy to have you here.

Horrible murder today, the body's face is completely smashed - It would be impossible to ID the person.
It happened around 1:55pm
Although, one of our patients is not present in their rooms and we have identified that it must be Mr.Hardy.
He was a lovely person and we are all deeply saddened and shocked by this incident today.
We have reached out to his family today, to tell them the news. They never visited him.
The body is in the main hall, we did not want to move it incase it gives you any clues.

I know you just got here, but this is very important information and I need to share it with you right away.
I saw four suspects running away from the body down towards the testing facillaties.
I chased them down to see their faces and they ran into the testing laboratory rooms.
They were either trying to hide or run away I am not sure, but When they ran into the testing rooms,
I shut the doors behind them, I guess they did not know that it is a one way door system.
They can not come back out. All four suspects are locked in their for you. The only problem is,
I do not run the testing labs I am never down here.
Dr.Robertson does, and you need a special Key Card to open the doors which only he has. 
Now, unfortunatly Dr.Robertson is away on Holiday for the past week but he is back tomorrow.
This will give you a lot of time to be able to put the pieces together and hopefully solve this brutal Murder.
You are free to move around Hallow Halls as much as you want to gather evidence, 
and come to your conclusion of WHO MURDERED MR.HARDY.
""")
        decision = input("""\nOk, time to explore this facility and see what I can find.\n
Do you want to go to the Main hall / the Living Room or the Testing Labs? \n
(Type main hall or living room or testing labs) \n""").lower()
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
            print("""Invalid input - You must choose between the main hall or the living room or testing labs.\n
(Type main hall or living room or testing labs into terminal) \n""")
            

# Common Room function
def common_room():
    clear_screen()
    while True:
        clues()
        decision = input("""You made your way back to the Common Room. \n
Would you like to go to the Living room / the Main hall \ the Testing Labs?
(Type Main Hall or Living Room or Testing Labs) \n""").lower()
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
            print("""Invalid input - You must choose between the main hall or the living room or testing labs.
(Type main hall or living room or testing labs into terminal) \n""")
        

# Instructions function
def instructions():
    print("instructions")


# Main hall function
def main_hall():
    clear_screen()
    while True:
        clues()
        print("""You have arrived in the main hall and see the body...
hmm...
The body is at the bottom of the stairs..
It looks like somebody may have pushed the victim down the stairs?
Mabye I should take a closer look at the body to see if I can find any clues \n""")
        decision = input("""Should I search the body or make my way up to the bedrooms upstairs?
\n(Type 'body' or 'bedroom') \n""").lower()
        if decision == "body":
            clear_screen()
            if "Grey hair, Glasses, Tube" not in inventory:
                inventory.append("Grey hair, Glasses, Tube")
            if """Note about the body: Looks like mabye the killer was trying to frame someone by placing the body at the end of the stairs?""" not in notes:
                notes.append("""Note about the body: Looks like the killer was trying to frame someone by placing the body at the end of the stairs?""")
            clues()
            print("""You make your way over to the body to take a closer look.
Oh wow... This body was not pushed down the stairs, rather it WAS STABBED to death.
There is multiple stab wounds in the victims back.

Hmm.... interesting,
it looks like the murderer was trying to mabye frame someone by placing the body at the end of the stairs?
Not a bad idea... Who would want us too think that the body had been pushed down the stairs to its death?

Lets take a look in the victims pockets for any clues, looks like a pair of old glasses and a testing tube?
His clothes seem ripped too.
I'm going to keep these items in my bag for now.
Oh look one last piece of his grey hair, actually it looks like he was bald from what I can make out.
Mabye I should go upstairs and look around the bedrooms!
\n""")
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
                elif decision2 == "quit": 
                    quit()
                else: 
                    clear_screen()
                    clues()
                    print(" \n Invalid input - please type 'bedroom' or 'common room' into the terminal \n")
        elif decision == "bedroom":
            bedroom()
            break
        elif decision == "quit": 
            quit()
        else:
            clear_screen()
            print("Invalid input - please type 'body' or 'bedroom' into the terminal")


# Living room function
def living_room():
    clear_screen()
    while True:
        clues()
        print("""You make your way to the living room and see Dr.Mengeles wife.
\n You: 'Hello Ms.Mengele, I am the detetive you called. It is a pleasure to meet you.'

Ms.Mengele: 'Hello Detective, It was not actually me you called it was our maid,
I sent her home as she was in a lot of shock.
You are very welcome here at the wealthiest Pyschiatric Facility in Europe.
Please do ask any questions you may have about the suspects. I do hope Dr.Robertson arrives back tomorrow,
so you can put away the murderer, bring peace back to Hallow Halls and to Mr.Hardys family.\n'""")
        decision = input("""\nDo you want to ask Ms.Mengele about the suspects,
or go to Dr.Robertson's Room?
\n(Type suspects or Dr.Robertson) \n""" ).lower()
        if decision == "suspects":
            clear_screen()
            clues()
            print("""You: 'So Ms.Mengele can you tell me a bit about the suspects?'\n

Ms.Mengele: ' um Yes Dectetive of course.
Well first of all the four suspects are named Tom, Alice, Nicki, and Josh.
All pateints here in Hollow Halls.

Let me start with Tom, Tom is one of our disbaled pateints here, he is in a wheelchair,
he got paralysed from the waist down when he was serving in the war. He suffers from PTSD and his room is downstairs,
unfortunatly we have no elevators here yet.

Then we have Alice, poor Alice. 
I wouldnt believe everything she says she can be a bit out of it most of the times,
if you know what I mean.
She has a history of drug abuse,
she is also best of friends with Josh they never leave eachothers sides.
They share a bedroom down the hall. 
She also had beef with Mr.Hardy!!
            
Nicki, well suprised me the most she is quite and calm,
but you know detective sometimes the quite ones can do the most harm, she lives upstairs and has ocd everthing is
spotless, she is quite small though around 5ft.

Lastly, we have Josh. Best friends with Alice.
Josh is mute. Josh can not speak unfortuneatly.
Not much else to say about that... '

You: All interesting points there. I should try and remember this conversation.""")
        
            while True:
                decision2 = input("""\nGo to Alice and Joshs room or back to common room \n
(Type Alice and josh or common room) \n""").lower()
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
                    clues()
                    print("Invalid input - You should have typed alice and josh or common room")
        elif decision == "dr.robertson":
            dr_robertson()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print("Invalid input please type in suspects or calm")


# Alice and Joshs room function
def alice_josh():
    clear_screen()
    if "straight edge society badge" not in inventory:
        inventory.append("straight edge society badge")
    if "Notes about Alice and Josh's room: 'Drawing drawn at 2:15pm murder was at 1:55pm'" not in notes:
        notes.append("Notes about Alice and Josh's room: 'Drawing drawn at 2:15pm murder was at 1:55pm'")
    while True:
        clues()
        print("""\nYou make your way to Alices and Josh's shared room. You Look at Josh's side first.
Everything looks normal, Josh seems to like his comics, he has a lot of them, nothing out of the ordinary.
Oh wow amazing, he has drawn the avengers superheros, he is very talented. Drawn at 2:15pm is says on todays date...
but Dr.Mengele said the murder was at 1:55pm and that they ran straight down to the testing labs?

You make your way over to Alices side.
A straight edge society badge. Hmm, that is conflicting from what I have heard. \n
""")
        decision = input("\nLet's go back to the common room to re-asses (Type common room) \n").lower()
        if decision == "common room":
            common_room()
            break
        elif decision == "quit":
            quit()
        else:
            clear_screen()
            print("\n Invalid Input - type Common Room \n")

    
# Dr.Robertson's Room Function
def dr_robertson():
    clear_screen()
    if "'I am a box who holds keys but not locks. With the right combination, I may unlock your soul. What am I?'" not in riddle:
        riddle.append("'I am a box who holds keys but not locks. With the right combination, I may unlock your soul. What am I?'")
    while True:
        clues()
        print("""You make your way into Dr.Robertson's Room.
It is a very safisticated looking room, nice and tidy. Lots of graphs on the walls,
he must live and breathe his work. No posters or pictures of anything,
just an unopened box of contact lenses.
I hope he is enjoying his Holiday Break, it looks like he needs it.

As you search his room for clues you come across a piece of laminated paper in one of his wardrobes.
It has a picture of a safe on it and a testing tube. Looks to be some sort of riddle on it,
I wonder does this riddle lead to anything? I will keep it with me just incase.

'I am a box who holds keys but not locks.
With the right combination, I may unlock your soul.
What am I?' \n""")
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


 # Testing Labs function       
def testing_labs():
    clear_screen()
    if "Ripped piece of clothing, " not in inventory:
        inventory.append("Ripped piece of clothing, ")
    while True:
        clues()
        print("""You make your way down into the testing labs. It looks dark and lonely down here.
I guess not a lot of people come down here bar Dr.Robertson.
On the ground in front of you, you see some fabric of clothing on the floor,
looks like it has been ripped off? Hmm could be nothing...

In the corner of your eye you see what looks like some sort of safe.
Mabye there is something important in there? 

To your right you see the doors in which the suspects are locked in. You need that special key Dr.Robertson has""")

        decision = input("""\nDo you want to look at the safe or go to the suspects?\n
(Type Safe or Suspects room)\n""").lower()

        if decision == "safe":
            clear_screen()
            clues()
            print("""\nYou make your way over to the safe.
This looks tricky... it looks like I need to type in a word.\n""")
            while True:
                decision2 = input("""\nInput the word you think is needed to open the safe\n""").lower()
                if decision2 == "piano":
                    print("""\nLooks like a diary, lets take a look.
'Date march 5th 2024. \n
Time of day: 7pm.\n

Today marks the most important day in my life, in fact mabye one of the most important days in human history.
After years and years of research I have figured out how to stop mental illness. I have found the cure.
No more will people be plaughed by this horrible illness.
No more will facilities and big pharma, take everyones money.
Tomorrow I put an end to millions of peoples suffering,
I know I might get some back lash from people who profit from mental illness,
but I hope they can see the bigger picture and realize that this is what is best for the world.
I am excited to tell the world tomorrow. \n""")
                    if "Dr.Robertson's Discovery, Spare Key card" not in inventory:
                        inventory.append("Dr.Robertson's Discovery, Spare Key card")
                    while True:
                        decision3 = input("""\n WOW THIS IS VERY IMPORTANT - Lots of clues in that diary.
hmm ... some things just dont quite add up ...Time to make my way back to the common room.
I need to put all my clues together.
I think I know what happened here at Hallow Hall, after I come to a conclusion lets go see the suspects.\n
Type (common room)\n""").lower() 
                        if decision3 == "common room":
                            common_room()
                            break
                        elif decision3 == "quit":
                            quit()
                        else:
                            clear_screen()
                            clues()
                        print("\nInvalid input - Type common room\n")
                elif decision2 == "quit":
                    quit()
                else:
                    while True:
                        print("Damn looks like I got it wrong, mabye I can find a clue for this somewhere \n")
                        wrong = input("Type common room to go back and search for more clues \n").lower()
                        if wrong == "common room":
                            common_room()
                            break
                        elif wrong == "quit":
                            quit()
                        else:
                            clear_screen()
                            clues()
                            print("\ninvalid input - type common room\n")

        elif decision == "suspects room":
            suspects()
            break
        elif decision =="quit":
            quit()
        else:
            clear_screen()
            print("\ninvalid input - Please type safe or suspects room\n")

                
# Suspects Room Function            
def suspects():
    clear_screen()
    while True:
        clues()
        if len(inventory) < 5:
            print("""I do not think I have searched Hallow Halls enough yet,
    lets come back later when we have more clues found \n
    (You Need all 8 items to enter) \n""")
            decision = input("\nType common room to continue search for clues\n").lower()
            if decision == "common room":
                common_room()
                break
            elif decision == "quit":
                quit()
            else:
                clear_screen()
                print("Invalid input - Type common room")
        else:
            print("""You bring Mr.Mengele down to the suspects room.
You:'So Mr.Mengele I have some great news, I found Dr.Robertsons special keycard to open the doors.
Let's get this over with right now, I know who the killer is.'

Dr.Mengele: 'Oh are you sure? are you positive you dont want to wait the night and sleep on it?'

You: 'No I am 100% positive on who the killer is - before we go in their let me explain my reasoning to you...'

After explaining everything to Dr.Mengele. You make your way into the suspects room.
All four suspects look heavily sedated and dazed... as expected... 
""")
            decision2 = input(""" \nIt is time for you to choose WHO WAS THE MURDERER??!! \n""").lower()
            if decision2 == "dr.mengele":
                winner()
            else:
                loser()
                

def winner():
    clear_screen()
    print("""IT WAS YOU DR.MENGELE !!

You might be asking how did I figure it out? Well let me explain.....

First of all, You said you were out for a 'run', you were sweating, and out of breathe.
You were shocked by my early arrival, the only reason you were sweating was because you were in a rush to cover up this murder after you heard the maid call me.
When you were told I arrived earlier then expected you were shocked and ran around as quickly as possible to try and cover this all up but you failed.
This was the first lie of many. In fact you were running around trying to frame these four 'suspects' which you had locked
in the basement because they saw you murderer this victim.

Forty years here huh? You are quite old.. Nice set of grey hair you have Dr. Almost as if the only piece of hair on the victims body was infact grey,
and none of your 'suspects' have grey hair? You mentioned you did not go near or move the body? How would the grey hair get there then? The victim was aslso bald.

Now... you trapped them 'suspects' in there Dr, they did not run in there themselves. You drugged them after you saw them see you murder this victim.
As you can tell by how drugged up they all look right now you used some sort of amnesia drug so that they would forget about all this in the morning.
You had a keycard this whole time because your one is the exact same one I found to unlock this door.
You had them trapped in here because you knew they could not escape from the inside. But this whole time you were just lying to me about not being able to open the door,
and that only Dr.Robertson had a special keycard. You are the owner for christ sake of course you have a keycard. You wanted me to stay the night,
so that you could come up with a plan on what to do with these four 'suspects' during the night ... mabye you were going to kill them all and stage an 'escape'??
You needed them trapped so you could frame them one way or another and you needed time to think and come up with a plan as I got here very quickly.

I must say you done a fairly good job in trying to frame these suspects but you missed some key details which let me to this discovery that it was you and not them.

You moved the body to the bottom of the stairs, this is where the grey hair came from. You then tried to frame Tom. You knew you had stabbed the victim in the back.
You knew I would see the stab wounds and you thought I would think that Tom was actually the one doing the framing. You thought I would think that Tom placed the body,
at the bottom of the stiars, so that it looked like someone pushed the body to the stairs to his death. Of course Tom can not walk up the stairs and you used his disability
as a chance for me to think he was the one doing the framing. When in fact is was all you. Now of course it still could have been Tom..
but ...It was not Tom because the actual murder weapon was upstairs !! There would have been no way Tom could have stashed the Murder weapon up there. So that rules him out.

Now you ask what about Nicki? Nicki has OCD which your wife told me. Everything in Nickis rooms is super clean. I found blood droplets in the sink.. How would she has missed this?
Ah yes, because it was not her... it was you in a rush trying to clean the blood from the knife, you left some droplets in the sink because you were in such a rush.
You then tried to 'hide' the knife. But really you wanted me to see it, you wanted me to mabye think it was Nicki who murdered the victim. but again DR.
you made a mistake. It could not have been Nicki because you placed it in a really high place, Nicki could never reach that she is only 5ft.

Your wife is not much better. She was filling me with some lies too... She was trying to set up Alice telling me she was a bad drug user and that she could get crazy.
She also said she had 'beef' with Mr.Hardy the alledged victim. Now I am not sure if she had beef with Mr.Hardy but I do not care about that and I will explain later,
but Alice was not a drug user inface Alice was the opposite - Alice was part of the straight edge society which means she never done hardcore drugs in her life.

Josh and Alice were also togehter after the murder Josh was drawing a pciture of his favourite comic book heros this would have taken hours.
Josh and Alice sign the back of every single picture Josh drew with a date and time of completion.
There is no way they could have commited this murder because they were in there rooms at the time. You said the 'suspects' ran to the testing labs.
This is not true they must have heard the maids screem of seeing the body in the main hall and you saw them looking out of there rooms and drugged them and brought them down.

So it was not Tom, Nicki, Alice, or Josh. IT WAS YOU ! 

Now.... back to explaining why I did not care that Alice may or may not have had beef with Mr.Hardy... Mr.hardy has not been on your records for months..
I presume you may have killed him too... as he is no where to be found for months from your records and his family never visits him.
 He is an easy pateint to pretend that this is his body, no one would question it, not even the family. 

That body IS NOT MR.HARDY'S BODY! THAT BODY IS DR.ROBERTSON'S BODY!!

You killed Dr.Robertson because of what he had discovered!
You knew it would destroy your wealth!! 
He was about to save millions of lives and you murdered him in cold blood because of how selfish you are.
You are a sick man Dr.Mengele - Luckiliy I have figured it out and I will get Dr.Robertsons work in the hands of the right people.

You destroyed Dr.Robertsons face because you did not want him ID'd - You were going to dispose of his body during the night.
You used an excuse that he was on Holiday. You were going to use that as an excuse as to why he never returned.... and must have died over there.
I read his diary. He was here YESTERDAY  Dr.... You told me he has been gone for a week on Holiday... 

There was some piece of ripped clothing down here I found near the testing labs... It was his.
You stabbed him down here after he told you about the discovery he made. You could not let this happen. 
You stabbed him and a piece of his clothing came off with it, his body when I searched it in the main hall has a peice of clothing missing from his back.
You moved him up to the main hall, the maid saw the body and called me. You then had to quickly come up with a solution to frame someone else and get any
suspicion away from you.
He also had a pair of glasses and a testing tube in his pocket. You really should have taken them out Dr.Mengele... but I know you were in a rush.
Interesting how Dr.Robertson had some unopened contact lenses in his room. He must still stick to wearing his glasses...
The testing tube is a bit of a giveaway I dont think I need to explain that.

So there we have it... YOU MURDERED DR.ROBERTSON. 

“You have the right to remain silent. Anything you say can and will be used against you in a court of law.
You have the right to an attorney. If you cannot afford an attorney, one will be provided for you.
Do you understand the rights I have just read to you?”

..........................

CONGRATULATIONS YOU HAVE SOLVED THE HALLOW HALLS MURDER MYSTERY WELL DONE !! \n
GAME OVER.
""")
    while True:
        ending = input("Type quit to quit the game")
        if ending == "quit":
            quit()
        else:
            clear_screen()
            print("Invalid input type quit")

def loser():
    clear_screen()
    while True:
        print("Damn you got it wrong... try again next time... YOU JUST SENT AN INNOCENT PERSON TO PRISON HOW COULD YOU!!")
        ending = input("Type restart to restart the game").lower()
        if ending == "restart":
            clear_screen
            main_menu()
            break
        elif ending == "quit":
            quit()



# Bedroom
def bedroom():
    clear_screen()
    if "Knife" not in inventory:
        inventory.append("Knife")
    while True:
        clues()
        print("""You make your way up the stairs and search the bedrooms.
You dont seem to see anything suspicious until finally the last room.

In the last room as you are looking,
you see something shiny at the very top of the wardrobe,
stashed away in the far corner.
You check and you find a knife - AH HA!!
This must be the murder weapon, but the knife looks very clean and has no blood on it??

Let's keep this with us.
- The murderer must be very tall to reach up there.\n""")
        
        decision = input(""" \n The bathroom door seens to be open in this bedroom,
Do you want to have a look in there or do you want to make your way back to the common room?\n
(Bathroom / Common Room) \n""").lower()
        if decision == "bathroom":
            clear_screen()
            clues()
            if """ - Notes about the bathroom/bedroom:- Drops of Blood in sink - Killer in a rush - Who's Bedroom is that? Must be very tall""" not in notes:
                notes.append(""" - Notes about the bathroom/bedroom:- Drops of Blood in sink - Killer in a rush - Who's Bedroom is that? Must be very tall""")
            print("""Medicine cabnit looks empty, nice and clean...
what is that?

Oh wow, uhh jesus there looks like there is some drops of blood in the sink..
This may be where the killer sleeps this may be the killer..
It looks like they were in a rush and did not clean properly.

- Ok lets make my way back downstairs and into the common room to re-asses. \n""")

            while True:
                home = input("\nTime to make my way back to the Common Room (Type Common Room to get there) \n").lower()
                if home == "common room":
                    common_room()
                    break
                elif home == "quit":
                    quit()
                else:
                    clear_screen()
                    clues()
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



