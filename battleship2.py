
from GameClass import Game
# The code where the game is executed


print("====================================================")
print("                Battleship DX special               ")
print("====================================================")

print("\n")

start = input("Enter anything to start the game.")

print("\n")

again = "y"
while again.lower() == "y":

    difficulty = input("Please enter the difficulty of the game. (Easy: e /Medium: m/Hard : h) ")
    while difficulty.lower() not in ["e","m","h"] :
        difficulty = input("Sorry. I didn't catch that. Please enter again. (Easy: e /Medium: m/Hard : h) ")
    if difficulty.lower() in ["m","h"] :
        bonus = input("Would you like to activate magic boxes in this game? (Yes: y/No: n) ")
        while bonus.lower() not in ["y","n"]:
            bonus = input("Sorry. I didn't catch that. Please enter again. (Yes: y/No: n) ")
    elif difficulty.lower() == "e":
        bonus = "n"


    print("\n")

    game = Game(difficulty.lower(),bonus.lower())

    game.gameSetup()

    again = input("Would you like to try again? (Yes: y/No: n) ")

    while again.lower() not in ["y", "n"]:
        again = input("Sorry. I didn't catch that. Please enter again. (Yes: y/No: n) ")








