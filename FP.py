Bad = 0
Good = 0
intell = 0
stren = 0
class PlayerType:
    def __init__(self, intelligence, strength):
        self.intelligence = intelligence
        self.strength = strength
strong = PlayerType(5, 10)
smart = PlayerType(10, 5)
balanced = PlayerType(8, 8)
print("Welcome to this game!")
name = input("What's your name? ")
print(f"{name}! What a great name!")
print("You are free to do whatever you want in this game. Your choices throughout the story affect what is available to you later and change the paths that you can embark on. Are you ready to begin the game?")
print("1: Yes")
print("2: No")
playgame = input()
if playgame == "1":
    print("Great! What kind of person would you like to be?")
    print("1: Smart")
    print("2: Strong")
    print("3: Balanced")
    player = input()
    if player == "1":
        stren += 5
        intell += 10
    elif player == "2":
        stren += 10
        intell += 5
    elif player == "3":
        stren += 8
        intell += 8
    print("Great! Your story begins in high school...")
    print("It's your first day of freshman year, and you get a pop quiz. You know your friend will get the answers right, and he's sitting right next to you. You probably won't get caught either. Do you take the chance and look at your friend's paper or take the L?")
    print("1: Cheat")
    print("2: Take the L")
    cheat = input()
    if cheat == "1":
        Bad = Bad + 1
        print("You decide to take a tiny look at your friend's paper and manage to find a couple answers that you didn't know. You look up to find your teacher standing in front of you, shaking his head. Your test is ripped up and you are sent to the office.")
        print("On your way to the office, you notice an open window. You could jump out and skip going to the principal's, or own up to what you did and take the punishment. What's it gonna be?")
        print("1: Jump out")
        print("2: Go to principal's")
        window = input()
        if window == "1":
            print("Free at last! On your first day, you cheated on a quiz and skipped school. You're really quite the troublemaker. All this mischief has made you pretty hungry. Do you wanna go get some lunch or go home?")
            print("1: Get lunch")
            print("2: Go home")
            lunch = input()
            if lunch == "1":
                print("You go to get lunch. On the way, you hear a mysterious voice calling your name. What do you do?")
                print("1: Follow the voice")
                print("2: Go get lunch")
                voices = input()
                if voices == "1":
                    print("You decide to follow the voice and it leads you to a long, dark tunnel. Do you continue or turn back?")
                    print("1: Continue")
                    print("2: Turn back")
                    tunnel = input()
                    if tunnel == "1":
                        print("You follow the tunnel to the end and find an old looking sword and a big bar of gold. You can only carry one, so which one do you take?")
                        print("1: Sword")
                        print("2: Gold")
                        sword = input()
                        if sword == "1":
                            print("You grab the sword and start walking out of the tunnel when all of a sudden the entrance closes. Standing in its path is a huge man holding a knife, walking towards you. You can either fight the man or look for another way out. What's it gonna be?")
                            print("1: Fight the man")
                            print("2: Look for another way")
                            fight = input()
                            if fight == "1" and stren >= 8:
                                print("You charge at the man with the sword. Luckily, you're strong enough to knock his knife out of his hand with the sword. You run past him and escape the tunnel with a new weapon.")
                                print("Suddenly, you hear the whispering again. You sense that this could be an opportunity to earn another item. Do you follow the whispers or cut your losses?")
                                print("1: Follow whispers")
                                print("2: Go home")
                                whis = input()
                                if whis == "1":
                                    print("The whispers get louder at the entrance to a sewer. You enter and in your path is a shield that seems to match your sword. You pick it up and begin to walk out when the ground crumbles beneath you! You pick yourself up and see a 50 foot monster towering above you. There's a door behind you, or you could fight the monster and potentially get a reward. What do you say?")
                                    print("1: Fight")
                                    print("2: Get out")
                                    monster = input()
                                    if monster == "1":
                                        print("You run up to the monster and, with your strength, drive your mighty sword through its heart! The monster crumbles to the floor, and behind him is a piece of paper. You pick it up, and all your surroundings begin to disintegrate. You wake up to the sound of the whispers. It's your mom, waking you up for school. Was it all a dream? You look over to your nightstand and find your reward: the answers to the test. Congradulations! You're gonna pass the test!")
                                else:
                                    print("You go home with a sword in your possession. You still failed the test, but hey, at least you have a sword, right?")
                            else:
                                print("You are not strong enough to fight the man, so you are forced to look for another way out. As you search around the tunnel and await your death, you realize that maybe you should have been a little stronger or taken the gold.")
                        else:
                            print("You take the gold and walk out of the tunnel. A quick google search reveals that if you sold your gold, you would have 10 million dollars! What do you say?")
                            print("1: Sell it")
                            print("2: Keep it")
                            sellgold = input()
                            if sellgold == "1":
                                print("You sell the gold, and now you have enough money to buy your own house, settle down, and never work a day in your life! Congrats!")
                            else:
                                print("... ok... you kept the gold? I guess you'll just have a cool giant gold bar in your room from now on. Good for you, I guess.")
                else:
                    print("Wow, you sure are boring. Maybe next time you'll be a little more risky and make some more daring choices.")
            else:
                print("You go home, and you arrive to your mother waiting for you. You've never seen her so angry in your life. You're grounded for a year. Maybe you should be a little more honest next time.")
        else:
            print("You go to your principal's and get suspended for a week. You are immediately sent home. On the walk, you hear a mysterious voice calling your name. What do you do?")
            print("1: Follow the voice")
            print("2: Go home")
            voicess = input()
            if voicess == "1":
                print("You decide to follow the voice and it leads you to a long, dark tunnel. Do you continue or turn back?")
                print("1: Continue")
                print("2: Turn back")
                tunnel = input()
                if tunnel == "1":
                    print("You follow the tunnel to the end and find an old looking sword and a big bar of gold. You can only carry one, so which one do you take?")
                    print("1: Sword")
                    print("2: Gold")
                    sword = input()
                    if sword == "1":
                        print("You grab the sword and start walking out of the tunnel when all of a sudden the entrance closes. Standing in its path is a huge man holding a knife, walking towards you. You can either fight the man or look for another way out. What's it gonna be?")
                        print("1: Fight the man")
                        print("2: Look for another way")
                        fight = input()
                        if fight == "1" and stren >= 8:
                            print("You charge at the man with the sword. Luckily, you're strong enough to knock his knife out of his hand with the sword. You run past him and escape the tunnel with a new weapon.")
                            print("Suddenly, you hear the whispering again. You sense that this could be an opportunity to earn another item. Do you follow the whispers or cut your losses?")
                            print("1: Follow whispers")
                            print("2: Go home")
                            whis = input()
                            if whis == "1":
                                print("The whispers get louder at the entrance to a sewer. You enter and in your path is a shield that seems to match your sword. You pick it up and begin to walk out when the ground crumbles beneath you! You pick yourself up and see a 50 foot monster towering above you. There's a door behind you, or you could fight the monster and potentially get a reward. What do you say?")
                                print("1: Fight")
                                print("2: Get out")
                                monster = input()
                                if monster == "1":
                                    print("You run up to the monster and, with your strength, drive your mighty sword through its heart! The monster crumbles to the floor, and behind him is a piece of paper. You pick it up, and all your surroundings begin to disintegrate. You wake up to the sound of the whispers. It's your mom, waking you up for school. Was it all a dream? You look over to your nightstand and find your reward: the answers to the test. Congradulations! You're gonna pass the test!")
                            else:
                                print("You go home with a sword in your possession. You still failed the test, but hey, at least you have a sword, right?")
                        else:
                            print("You are not strong enough to fight the man, so you are forced to look for another way out. As you search around the tunnel and await your death, you realize that maybe you should have been a little stronger or taken the gold.")
                    else:
                        print("You take the gold and walk out of the tunnel. A quick google search reveals that if you sold your gold, you would have 10 million dollars! What do you say?")
                        print("1: Sell it")
                        print("2: Keep it")
                        sellgold = input()
                        if sellgold == "1":
                            print("You sell the gold, and now you have enough money to buy your own house, settle down, and never work a day in your life! Congrats!")
                        else:
                            print("... ok... you kept the gold? I guess you'll just have a cool giant gold bar in your room from now on. Good for you, I guess.")
            else:
                print("Wow, you sure are boring. Maybe next time you'll be a little more risky and make some more daring choices.")
    else:
        Good = Good + 1
        print("You stick to your morals and decide to fail the test. Your parents are gonna kill you, but hey, at least you're honest!")
        print("You come home and find a message on your home phone about your test. You could delete the message and maybe your parents will never find out, or you could leave it there and guarantee that you will be grounded. What will you choose?")
        print("1: Delete the message")
        print("2: Leave it")
        message = input()
        if message == "1":
            Bad += 1
            print("You delete the message just before your mom gets home. You think you're in the clear until your school calls again the next day. When you get home, your mom grounds you for a whole year for cheating, skipping school and deleting the message. Maybe you should choose more carefully next time.")
        else:
            Good += 1
            print("You leave the message alone and when your mom hears it, she's very disappointed in you. However, she commends you for your honesty and you do not get grounded.")
            print("The next day, you're walking to school and hear a mysterious voice whispering your name. You can either continue walking to school or follow the voice. What's it gonna be?")
            print("1: Follow the voice")
            print("2: Go to school")
            voice = input()
            if voice == "1":
                print("You decide to follow the voice and it leads you to a long, dark tunnel. Do you continue or turn back?")
                print("1: Continue")
                print("2: Turn back")
                tunnel = input()
                if tunnel == "1":
                    print("You follow the tunnel to the end and find an old looking sword and a big bar of gold. You can only carry one, so which one do you take?")
                    print("1: Sword")
                    print("2: Gold")
                    sword = input()
                    if sword == "1":
                        print("You grab the sword and start walking out of the tunnel when all of a sudden the entrance closes. Standing in its path is a huge man holding a knife, walking towards you. You can either fight the man or look for another way out. What's it gonna be?")
                        print("1: Fight the man")
                        print("2: Look for another way")
                        fight = input()
                        if fight == "1" and stren >= 8:
                            print("You charge at the man with the sword. Luckily, you're strong enough to knock his knife out of his hand with the sword. You run past him and escape the tunnel with a new weapon.")
                            print("Suddenly, you hear the whispering again. You sense that this could be an opportunity to earn another item. Do you follow the whispers or cut your losses?")
                            print("1: Follow whispers")
                            print("2: Go home")
                            whis = input()
                            if whis == "1":
                                print("The whispers get louder at the entrance to a sewer. You enter and in your path is a shield that seems to match your sword. You pick it up and begin to walk out when the ground crumbles beneath you! You pick yourself up and see a 50 foot monster towering above you. There's a door behind you, or you could fight the monster and potentially get a reward. What do you say?")
                                print("1: Fight")
                                print("2: Get out")
                                monster = input()
                                if monster == "1":
                                    print("You run up to the monster and, with your strength, drive your mighty sword through its heart! The monster crumbles to the floor, and behind him is a piece of paper. You pick it up, and all your surroundings begin to disintegrate. You wake up to the sound of the whispers. It's your mom, waking you up for school. Was it all a dream? You look over to your nightstand and find your reward: the answers to the test. Congradulations! You're gonna pass the test!")
                            else:
                                print("You go home with a sword in your possession. You still failed the test, but hey, at least you have a sword, right?")
                        else:
                            print("You are not strong enough to fight the man, so you are forced to look for another way out. As you search around the tunnel and await your death, you realize that maybe you should have been a little stronger or taken the gold.")
                    else:
                        print("You take the gold and walk out of the tunnel. A quick google search reveals that if you sold your gold, you would have 10 million dollars! What do you say?")
                        print("1: Sell it")
                        print("2: Keep it")
                        sellgold = input()
                        if sellgold == "1":
                            print("You sell the gold, and now you have enough money to buy your own house, settle down, and never work a day in your life! Congrats!")
                        else:
                            print("... ok... you kept the gold? I guess you'll just have a cool giant gold bar in your room from now on. Good for you, I guess.")
            else:
                print("Wow, you sure are boring. Maybe next time you'll be a little more risky and make some more daring choices.")
else:
    print("Congratulations! The only way to win the game is not to play...")