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