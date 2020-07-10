from boardclass import Board

# create ship object: we will define ship as having a rectangular shape.
class Ship(object):
    def __init__(self,ship_row,ship_column,ship_length,ship_width):
        self.length = ship_length
        self.width = ship_width
        # initiate the position of the ship
        # the position of the ship is determined by the coordinates of its top left corner.
        self.row = ship_row
        self.column = ship_column
    # initially set the ship condition as not hit by the player.
    hit = 0
    #rotate the ship object
    def rotate(self):
        self.length = self.width
        self.width = self.length

    #check whether the ship placement has exceed the board boundary.
    def checkBoundary(self,board):
        tf = 0
        row = self.row
        column = self.column

        for a in range(row, row + self.length):
            if a > board.size -1:
                tf = 1
                break
        if tf == 0 :
            for b in range(column, column + self.width):
                if b > board.size -1:
                    tf = 1
                    break
        # Return true if exceed the board boundary, return false if not.
        if tf == 1 :
            return True
        else:
            return False

    # Define the hit function to determine whether the player has hit the ship,input the guess coordinates.
    def hitShip(self,x,y):
        tf = False
        row = self.row
        column = self.column

        for a in range(row, row + self.length):
            for b in range(column, column + self.width):
                if x == a and y == b :
                    tf = True
                    break
            if tf == True:
                #change the hit variable
                self.hit = 1
                break
        # return true if the player has hit it.
        return tf

    # Define a function to check whether the ship has overlapped each other.
    def checkShip(self,ship):
        tf = False
        row = self.row
        column = self.column

        for a in range(row, row + self.length):
            for b in range(column, column + self.width):
                if ship.hitShip(a,b) == True :
                    # make sure the ship is not "hit" from hitShip()
                    ship.hit = 0
                    tf = True
                    break
            if tf == True:
                break

        # return true if the ship has overlapped the other.
        return tf

    # define a function to check a list of ships using self.checkShip()
    def checkShips(self,ships):
        tf = False
        if ships != []:
            for ship in ships:
                if self.checkShip(ship) == True :
                    tf = True
                    break
        return tf




    # Define the ship placement on the board
    def placeShip(self,board):
        row = self.row
        column = self.column
        # hit_count represents whether the ship is hit or not. 0 for not hit. 1 for hit
        if self.hit == 0:
            for a in range(row, row + self.length):
                for b in range(column, column + self.width):
                    board.board[a][b] = "##"
        elif self.hit == 1:
            for a in range(row, row + self.length):
                for b in range(column, column + self.width):
                    board.board[a][b] = "**"








