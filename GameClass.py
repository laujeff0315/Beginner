from random import randint, choice
from boardclass import Board
from shipclass import Ship
from BonusClass import Bonus

# Define a game environment and the game setup
class Game(object):
    def __init__(self,difficulty,bonus):
        self.difficulty = difficulty
        self.bonus = bonus

    def gameSetup(self):
        # set the board size, number of lives, number of bonus items number of ships and ship sizes depending on the difficulty.
        if self.difficulty == "e":
            board_size = 4
            ship_number = 3
            ship_sizes = 2
            lives = 7
        if self.difficulty == "m":
            board_size = 7
            ship_number = 4
            ship_sizes = 3
            lives = 10
            num = 10 # number of bonus items
        if self.difficulty == "h":
            board_size = 10
            ship_number = 5
            ship_sizes = 3
            lives = 15
            num = 15


        # set up a board
        board = Board(board_size)

        # generate a list of ships
        ship_list = []

        # allocate ths ships on the board
        for x in range(ship_number):
            length = randint(1, ship_sizes)
            coordinate_list = [list(range(board.size)),list(range(board.size))]
            temp_ship = Ship(choice(coordinate_list[0]), choice(coordinate_list[1]), length, 1)
            rotate = randint(0,1) # decide whether the ship rotates
            if rotate == 1:
                temp_ship.rotate()
            # check whether the ship has exceed the boundary, if yes, reallocate the coordinates of the ship
            while temp_ship.checkBoundary(board) == True or temp_ship.checkShips(ship_list) == True :
                temp_ship = Ship(board.random_row(), board.random_col(), temp_ship.length, temp_ship.width)
            else:
                ship_list.append(temp_ship)
                # remove the coordinates from the list to reduce the likelihood of overlapping the other ships.
                for a in range(temp_ship.row, temp_ship.row + temp_ship.length) :
                    coordinate_list[0].remove(a)
                for b in range(temp_ship.column, temp_ship.column + temp_ship.width):
                    coordinate_list[1].remove(b)

        # allocate the bonus items!
        if self.difficulty != "e" and self.bonus == "y":
            bonusItems = Bonus(num,self.difficulty)
            item_list = bonusItems.placeItems(board,ship_list)

        print("Game start! Your aim is to find where the ships are and sink them!")


        # Running the game
        while lives > 0 and len(ship_list) > 0:
            valid = False
            print("\n")
            print("Number of Ships left: " + str(len(ship_list)))
            print("Lives: " + str(lives))
            print("Enter the row and column number to locate your guess.")
            print("\n")
            print(board)
            # Check whether the guessed position either has been chosen before or is a spot of the sunk ship
            while valid == False:
                guess_row = input("Please enter your row number: ")
                guess_column = input("Please enter your column number: ")

                if guess_row.isdigit() == True or guess_row.isdigit() == True :
                    guess_row = int(guess_row)
                    guess_column = int(guess_column)


                if guess_row not in range(0,board.size) or guess_column not in range(0,board.size):
                    print("Invalid Position. Please try again.")
                elif board.board[guess_row][guess_column] == "--" or board.board[guess_row][guess_column] == "??":
                    print("You have picked this spot before. Please try again.")
                elif board.board[guess_row][guess_column] == "**":
                    print("It seems that there is a sunken ship here. Try other spots. I think there won't be other "
                          "ships here.")
                else:
                    valid = True
                    print("\n")



            # condition if the player successfully hit a ship: remove the ship from the ship_list, and print the board
            # also condition if the player has picked a bonus item
            # with the chosen ship
            for ship in ship_list:
                if ship.hitShip(guess_row,guess_column) == True :
                    ship.placeShip(board)
                    ship_list.remove(ship)
                    print("Well done! You have sunk one of the ships!")
                    break
            else:
                if self.difficulty != "e" and self.bonus == "y" and bonusItems.hitItem(guess_row,guess_column,item_list,board) == True:
                    lives = bonusItems.itemEffect(lives,ship_list,board)
                else:
                    lives -= 1
                    board.board[guess_row][guess_column] = "--"
                    print("You missed the ships!")

        # Decide whether the player has won when the game is over.
        else:
            if lives <= 0:
                print("\n")
                print("Game Over. Ships are here marked as ##. ")
                for ship in ship_list:
                    ship.placeShip(board)
                print (board)

            elif len(ship_list)<= 0:
                print("\n")
                print("Congratulations! You have won!")
                print(board)



