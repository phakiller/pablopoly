import random
import os
import pyforms
from pyforms import settings as formSettings
from pyforms import BaseWidget
from pyforms.controls import ControlButton, ControlList, ControlLabel, \
    ControlProgress, ControlWeb

# Set my dafault CSS File
cssFilePath = os.path.join(
    os.path.dirname((os.path.realpath(__file__))), 'pablopolyStyle.css')
formSettings.PYFORMS_STYLESHEET = cssFilePath
formSettings.PYFORMS_STYLESHEET_DARWIN = cssFilePath
formSettings.PYFORMS_STYLESHEET_LINUX = cssFilePath
formSettings.PYFORMS_STYLESHEET_WINDOWS = cssFilePath

def returnBoad():
    _list = []
    for i in range(1, 9):
        _tuple = ()
        for j in range(1, 9):
            _tuple += (ControlLabel(f'{i} - {j}'),)
        _list.append(_tuple)
    return _list

class MainWindow(BaseWidget):

    def __init__(self):
        super(MainWindow, self).__init__('PABLOPOLY')
        print()
        # Setting defaults settings
        self._board = ControlList(label='Tabuleiro')
        self._playDice = ControlButton('Jogar Dado')
        self.mylabel = ControlLabel('One')
        self._teste = ControlWeb()
        self._teste.value = 'https://github.com/UmSenhorQualquer/pyforms'
        self._myMoney = ControlProgress(
            label='Your Money is on %p%', default=15, min=0, max=100)
        self._informations = ControlLabel(
            'Inital Money: $ 1500,00 | Max Money: $ 10000,00')

        self._board.value = returnBoad()

        self.formset = [(('_teste', '=', '_myMoney'), '_playDice'),
        '_informations',]
        print(self.formset)

        self._playDice.value = self.__playDices

    def __playDices(self):
        number = random.randint(1, 6)
        print()
        self._myMoney.value += 25
        return number

if __name__ == '__main__':
    pyforms.start_app(MainWindow)