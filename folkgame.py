#game design --> Starting Room (2 doors to exit, first includes a math question and second includes
#  a wordle problem) -> Next room is trivia or death, The question asks 4 trivia questions 
# and if the user fails to answer atleast 2 of them right they will die(and respawn to starting 
# room) Final room is an mystery code, each of the previous levels will give you a small hint and 
# a bit of info, the final room lets you have to sequece it all together and find the successfull pin
# to escape. (Or be trapped in the dungeon for all of eternaty mwahahah)

#establish varaibles
room = 'starting'
questions = 0 
game = 'running'

#game starts here
while game == 'running':
    #starting room 
    if room == 'starting': 
        print ("You have awoken in a dark desolate dungeon, will I ever make it out you think")
        
        print ("A quick look around this dungeon provides some insight, all you can see is 4 walls and an rickety wooden table in the far wall. On either side is a door. One door with an addition sign on it, math sprawled out all over the door or another door with letters and scribbles of all langauges spread throughout the door" )
        
        room = input("Which door will you choose, 1: math door, 2: language arts door, please answer 1 or 2 ")

    #first hurdle 
    if room == "1":
        room = 'room1door_1'
        room1door_1 = input("If a runner who runs at a constant speed of p miles per hour runs a mile in exactly p minutes, what is the integer closest to the value of p? (please provide answer in number not words) ")
        if room1door_1 == "8": 
            print ("The door unlocked and you have made it to the second room, 543")
            room = "room 2"
        else:
            print("error, you are wrong!, please try again")
            room = "1"

    elif room == "2":
        room = 'room_1door_2'
        room1door2 = input("What is the most commonly used word in the english language? ")
        if room1door2.lower() == "the":
            print ("The door unlocked and you have made it the second room, 543")
            room = "room 2"
        else: 
            print("error, you are wrong!, please try again")
            room = "2"

    #room 2 ghost story
    if room == "room 2": 
        print("The second room had a big shadow in the middle, right behind it was a pathway but somthing told me walking through the shadow would not be a great move here")
        print("The shadow spoke: 'son I will be asking you four questions today', if you get at least two out of the four I will reward you and let you pass, if not... lets not go there")

    #room 2 questions

        question_1 = input("What do you call a fake noodle? please only respond in one word ").lower()
        if question_1 == "impasta":
            questions += 1 
            print ("wow, bhahahhaha thats a sus one, you got it!!")
        else: 
            print ("that answer was wrong :( ")

        question_2 = input("What state is known for its small drinks? please only respond in one word ").lower()
        if question_2 == "minnesota": 
            questions += 1
            print ("thats a shocker, another point ")
        else: print("and that is an incorrect answer")

        if questions == 2: 
            print ("wow you surprised me! move on to the last room! merry christmas! " )
            room = "room 3"
        else: 
            question_3 = input("What sounds like a sneeze and is made of leather? please only respond in one word ").lower()
            if question_3 == "shoe": 
                questions += 1
                print ("wow, another point ")
            else: print("and that is an incorrect answer")

            if questions == 2: 
                print ("wow you surprised me! move on to the last room! merry christmas! " )
                room = "room 3"
            else:
                question_4 = input("Where do fruits go on vacation? ").lower()
                if question_4 == "paris": 
                    questions += 1
                    print ("wow, another point ")
                else: print("and that is an incorrect answer")

                if questions == 2: 
                    print ("wow you surprised me! move on to the last room! merrychristmas! " )
                    room = "room 3"

                else: 
                    print ("U have failed, time to die!!!!!!!!!!!!!!!")
                    room = 'starting'
#room 3 final room
    if room == "room 3": 
        print("you move past the ghost and into the third room, the walls are full of paint, green and red paint to be exact. There was one peice of paper and a pen on the floor of the room")

        print("You walk over to the paper and see one instruction, write down the secret code, first a 3 letter combination and combined with a phrase. for example 345newyearseve")
        print("the code HAS to have been given to me somewhere in these right??? ")

        finalinput = input("What do you input for the code? ")
        if finalinput == "543merrychristmas":
            print("you have passed the dungeon!!!")
            print("A path extrudes from the ground and leads upwards through a hidden starway you didn't see before, you are now freee!!!!!!")
            game = "not running"
        else: 
            print( "your code was wrong, try again")


