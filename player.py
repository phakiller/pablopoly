class Player():

    def __init__(self, _id, initalMoney):
        self._id = _id
        self.money = initalMoney
        self.__currentPosition = 0
        self.__cycleCompleted = 0
    
    def strMoney(self):
        return 'B ' + self.money
    
    def move(self, movementNumber):
        future = self.__currentPosition + movementNumber
        if future <= 40:
            self.__currentPosition = future
        else:
            self.__currentPosition = future - 40
            self.__cycleCompleted += 1
        return self.__currentPosition
    
    def getCurrentPosition(self):
        return self.__currentPosition

    def getCycleNumber(self):
        return self.__cycleCompleted
