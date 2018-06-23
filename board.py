from dice import Dice
from player import Player
from houses import housesInformations
from testHouses import testeHouse

class Board():

    def __init__(self, maxMoney=10000.00, initalPlayersMoney=1500.00):
        self.maxMoney = maxMoney
        self.bank = maxMoney - initalPlayersMoney
        # Resources
        self.dice = Dice(6)
        self.player = Player(0, initalPlayersMoney)
        self.machine = Player(1, initalPlayersMoney)
        # self.houses = housesInformations.copy()
        self.houses = testeHouse.copy()
    
    def __rollDices(self):
        return self.dice.rollDice() + self.dice.rollDice()
    
    def playerMovement(self):
        return self.__doMovement(self.player), self.__machineMovement()
    
    def __machineMovement(self):
        return self.__doMovement(self.machine)
    
    def __doMovement(self, player):
        movment = self.__rollDices()
        oldCycle = player.getCycleNumber()
        player.move(movment)

        if (oldCycle - player.getCycleNumber()) != 0:
            player.money += 200.00

        paymentVerification = self.__verifyPayment(player)
        if paymentVerification:
            self.__makePayment(paymentVerification)
        elif (self.__rollDices() % 2) == 0:
            self.__buyHouse(player)
        return player.getCurrentPosition()
    
    def __makePayment(self, informations):
        devedor = self.player if informations['id'] == '0' else self.machine
        ganhador = self.player if informations['id'] != '0' else self.machine
        devedor.money -= informations['price']
        if informations['toPay'] != 'Bank':
            ganhador.money += informations['price']

    def __verifyPayment(self, player):
        houseInformation = self.getPlayerHouse(player)
        if houseInformation['rent']['ownerId'] != player._id and \
            houseInformation['rent']['ownerId'] != None:
            if houseInformation['rent']['ownerId'] == 'Bank':
                return {
                    'id': str(player._id),
                    'toPay': houseInformation['rent']['ownerId'],
                    'price': houseInformation['rent']['price']
                    }
            else:
                return {
                    'id': str(player._id),
                    'toPay': houseInformation['rent']['ownerId'],
                    'price': houseInformation['rent']['price']
                    }
        return None

    def __buyHouse(self, player):
        self.houses[player.getCurrentPosition()]['rent']['ownerId'] = player._id

    def getPlayerHouse(self, player):
        return self.houses[player.getCurrentPosition()]
    
    def getPrettyInformation(self, player):
        info = self.getPlayerHouse(player)
        pinfo = f"""Descricao: {info['informations']}<br>
        Preço: {info['rent']['price']}<br>
        Dono: {info['rent']['ownerId']}
        """
        return pinfo
