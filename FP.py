Bad = 0
Good = 0
print("Welcome to this game!")
name = input("What's your name? ")
print(f"{name}! What a great name!")
print("You are free to do whatever you want in this game. Your choices throughout the story affect what is available to you later and change the paths that you can embark on. Are you ready to begin the game?")
print("Yes")
print("No")
playgame = input()
if playgame == "Yes":
    print("Great! Your story begins in high school...")
else:
    print("Congratulations! The only way to win the game is not to play...")
print("It's your first day of freshman year, and you get a pop quiz. You know your friend will get the answers right, and he's sitting right next to you. You probably won't get caught either. Do you take the chance and look at your friend's paper or take the L?")
print("Cheat")
print("Take the L")
cheat = input()
if cheat == "Cheat":
    Bad = Bad + 1
    print("You decide to take a tiny look at your friend's paper and manage to find a couple answers that you didn't know. You look up to find your teacher standing in front of you, shaking his head. Your test is ripped up and you are sent to the office.")
    print("On your way to the office, you notice an open window. You could jump out and skip going to the principal's, or own up to what you did and take the punishment. What's it gonna be?")
    print("Jump out")
    print("Go to principal's")
    window = input()
    if window == "Jump out":
        print("Free at last! On your first day, you cheated on a quiz and skipped school. You're really quite the troublemaker. All this mischief has made you pretty hungry. Do you wanna go get some lunch or go home?")
else:
    Good = Good + 1
    print("You stick to your morals and decide to fail the test. Your parents are gonna kill you, but hey, at least you're honest!")