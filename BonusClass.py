from boardclass import Board
from shipclass import Ship
from random import randint, choice

# define bonus item in the game.
class Bonus(object):
    def __init__(self,num,difficulty):
        self.num = num #number of bonus item
        self.difficulty = difficulty # determines the effects of bonus item

    # allocate the items over the board, without overlapping the ships
    def placeItems(self,board,ships):
        board_size = board.size
        item_list = []
        coordinate_list = [list(range(board_size)), list(range(board_size))]

        for x in range(self.num):
            tf = True
            while tf == True:
                x = choice(coordinate_list[0])
                y = choice(coordinate_list[1])
                temp_item = [x,y]
                for ship in ships:
                    if ship.hitShip(temp_item[0], temp_item[1]) == True:
                        ship.hit = 0
                        break
                else:
                    tf = False
            else:
                item_list.append(temp_item)

        return item_list

    #decides whether the player has hit the item
    def hitItem(self,x,y,item_list,board):
        tf = False
        for item in item_list:
            if x == item[0] and y == item[1]:
                tf = True
                board.board[x][y] = "??"
                break
        return tf

    # Determine the effects if the player has hit an item
    # Input:  lives, item list, ship_list, board
    # Output: Lives
    # effect: gaining or losing lives, get the hints of the ship coordinate, sink of the ship, game over

    def itemEffect(self,lives,ship_list,board):
        print("\n")
        heart = lives
        if self.difficulty == "e":
            return lives
        if self.difficulty == "m" or self.difficulty == "h":
            print("There is a magic box here... ")


        # for medium level player, they wil be asked whether they want the effect to be done.
        if self.difficulty == "m":
            response = input("Would you like to open it up and see what's inside? (Yes: y/ No: n) ")
            while response.lower() not in ["y","n"] :
                response = input("Sorry I didn't catch that. Would you like to open it? (Yes: y/ No: n) ")
            if response.lower() == "n":
                return lives

        print("\n")

        cho = randint(1,4)
        if cho == 1:
            print("Lucky! You have gained an extra life.")
            heart += 1
        elif cho == 2:
            print("Ouch! This was a bomb and exploded as you opened it. You lost a life.")
            heart -=1
        elif cho == 3:
            ship_coord =[]
            for ship in ship_list:
                ship_coord = ship_coord + list(range(ship.row, ship.row + ship.length)) + list(range(ship.column, ship.column + ship.width))
            coord = choice(ship_coord)
            print("There is a number showing up...")
            print(str(coord) + "... I wonder if this means anything...")
        elif cho == 4:
            print("You opened it up and nothing happens...")

        #for hard-level player, there is a chance for them to enter a lottery which has riskier outcomes.
        if self.difficulty == "m":
            return heart
        elif self.difficulty == "h":
            chance = randint(0,3)
            if chance == 0:
                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\//\/\/")
                print("Congratulations! You have been chosen to enter a special lottery!")
                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\//\/\/")
                print("You can either take what you have now, or join this for a better prize! (and with higher risks as well!)")
                print("\n")
                response_1 = input("Would you like to take part in this?  (Yes: y/ No: n) ")
                while response_1.lower() not in ["y", "n"]:
                    response_1 = input("Sorry I didn't catch that. Would you like to take part in this? (Yes: y/ No: n) ")
                if response_1.lower() == "n":
                    print("\n")
                    print("Oh... That's a shame... ")
                    return heart
                else:
                    print("\n")
                    cho2 = randint(1,10)
                    if cho2 == 1:
                        print("Nice. You are rewarded with 10 extra lives!")
                        lives += 10
                        return lives
                    elif cho2 == 2 or cho2 == 10:
                        print("I am sorry... you have lost 5 lives ...")
                        lives -= 5
                        return lives
                    elif cho2 == 3:
                        print("Lucky! 3 extra lives for you!")
                        lives+= 3
                        return lives
                    elif cho2 == 4:
                        print("hmm...")
                        return 0
                    elif cho2 == 5:
                        print("Nothing happens...")
                        lives -= 2
                        return lives
                    elif cho2 == 6:
                        print("Nothing happens...")
                        lives += 1
                        return lives
                    elif cho2 == 7:
                        temp_ship = choice(ship_list)
                        print("%s and %s ... Try to guess this and something may happen! "%(temp_ship.row, temp_ship.column))
                        return lives
                    elif cho2 == 8:
                        x = board.random_row()
                        y = board.random_col()
                        print("%s and %s ... Try to guess this and something may happen! "%(x,y))
                        return lives
                    elif cho2 == 9:
                        print("Surprise!")
                        temp_ship = choice(ship_list)
                        hit = temp_ship.hitShip(temp_ship.row,temp_ship.column)
                        temp_ship.placeShip(board)
                        return lives
            else:
                return heart






