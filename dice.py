import random

class Dice():

    def __init__(self, faceNumber):
        self.faceNumber = faceNumber
    
    def rollDice(self):
        return random.randint(0, self.faceNumber)
