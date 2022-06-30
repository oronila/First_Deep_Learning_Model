import random
import math
# def createRandomMoveSet():
#     movements = []
#     for i in range(500):
#         movements.append(random.randint(0,3)) #   1 is 'W'; 2 is 'S'; 3 is 'A'; 4 is 'D'.   Generating the movements  
#     return movements

moveTotal = 400

class dot:
    def __init__(self):
        #self.moves = moves
        self.x = 240
        self.y = 400
        self.width = 15      # Keeping track of each dots position within its own object.
        self.height = 15
        self.vel = 5
        self.score = 0
        self.won = False
        self.moveswon = 0
    
    def calculateScore(self):
        if(self.won==False):
            self.score = 1000-math.sqrt(math.pow(250-self.x,2)+math.pow(20-self.y,2))
        else:
            self.score = 2000 - self.moveswon
        self.x = 240
        self.y = 400
        self.width = 10        # Keeping track of each dots position within its own object.
        self.height = 10
        self.vel = 5
        self.won = False
        self.moveswon = 0
    
    def botWin(self, winmoves):
        self.won = True
        self.moveswon = winmoves