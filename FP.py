print("Welcome to this game!")
name = input("What's your name? ")
print(f"{name}! What a great name!")
print("You are free to do whatever you want in this game. Your choices throughout the story affect what is available to you later and change the paths that you can embark on. Are you ready to begin the game?")
print("1: Yes")
print("2: No")
playgame = input()
if playgame == 1:
    print("Great! Your story begins in high school...")
else:
    print("Congratulations! The only way to win the game is not to play...")