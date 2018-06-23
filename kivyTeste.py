import kivy
kivy.require('1.10.0')

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar

boardPositions = {
    'row1': {
        'column1': {
            'text': 'Seja um Milionario',
            'user': False
        },
        'column2': {
            'text': 'Seja um Milionario',
            'user': False
        }
    },
    'row2': {
        'column1': {
            'text': 'Seja um Milionario',
            'user': False
        },
        'column2': {
            'text': 'Seja um Milionario',
            'user': False
        }
    }
}

class Position(Button):

    def __init__(self, **kwargs):
        super(Position, self).__init__(**kwargs)
        self.disabled = True
        self.background_color = (255, 255, 255, 1)


class Board(GridLayout):

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.cols = 11
        self.row_force_default = True
        self.row_default_height = 60
        self.col_force_default = True
        self.col_default_width = 80
        for row in range(11):
            for col in range(11):
                self.add_widget(
                    Position(text=f'{row} - {col}', font_size=14))


class Pablopoly(App):

    def build(self):
        final = GridLayout(cols=2)
        final.add_widget(Board())
        # final.add_widget(Button(text='Teste'))
        return final

if __name__ == '__main__':
    Pablopoly().run()
