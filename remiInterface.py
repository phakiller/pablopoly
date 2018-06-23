import remi.gui as gui
from remi import start, App
import os

from board import Board

class MyApp(App):
    def __init__(self, *args):
        #custom additional html head tags
        my_html_head = '<title>PABLOPOLY</title>'

        #custom css
        my_css_head = """
            <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            """

        #custom js
        my_js_head = """
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
            """
        res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
        mySettings = {
            'static_file_path': res_path,
            'html_head': my_html_head,
            'css_head': my_css_head,
            'js_head': my_js_head,
        }
        #static_file_path can be an array of strings allowing to define
        #  multiple resource path in where the resources will be placed
        super(MyApp, self).__init__(*args, **mySettings)

    def idle(self):
        #idle loop, you can place here custom code
        # avoid to use infinite iterations, it would stop gui update
        pass

    def main(self):
        #creating a container VBox type, vertical (you can use also HBox or Widget)
        main_container = gui.VBox(
            width='800px', height='500px', style={'margin':'0px auto','padding':'10px'})

        # Board
        self.board = Board()

        #Label
        self.lbl = gui.Label("  PABLOPOLY")
        self.lbl.add_class("glyphicon glyphicon-bitcoin label label-info")

        # User Labels
        self.playerCurrentMoneyLabel = gui.Label(f'B {self.board.player.money}')
        self.playerCurrentPositonLabel = gui.Label(f'{self.board.player.getCurrentPosition()}')
        self.playerCycleNumberLabel = gui.Label(f'{self.board.player.getCycleNumber()}')
        self.playerHouseInformationLabel = gui.Label(f'{self.board.getPrettyInformation(self.board.player)}')

        # Machine Label
        self.machineCurrentMoneyLabel = gui.Label(f'B {self.board.machine.money}')
        self.machineCurrentPositonLabel = gui.Label(f'{self.board.machine.getCurrentPosition()}')
        self.machineCycleNumberLabel = gui.Label(f'{self.board.machine.getCycleNumber()}')
        self.machineHouseInformationLabel = gui.Label(f'{self.board.getPrettyInformation(self.board.player)}')
        
        #Buttons
        self.bt1 = gui.Button("Jogar Dados", width="450px")
        self.bt1.add_class("btn-info")
        self.bt1.set_on_click_listener(self.rollDice)

        # Informations Table
        self.myList = [  ('ID', 'Jogador','Bitcoin(s)', 'Posição Atual', 'Voltas'),
                    ('0', 'Você', self.playerCurrentMoneyLabel, self.playerCurrentPositonLabel, self.playerCycleNumberLabel),
                    ('1', 'Máquina', self.machineCurrentMoneyLabel, self.machineCurrentPositonLabel, self.machineCycleNumberLabel)  ]

        self.tbl = gui.Table.new_from_list(content=self.myList,width='500px',height='100px',margin='10px')
        self.tbl.add_class("table table-striped")
        
        # Positions Table
        self.tableHouseInformation = [
            ('Your Position', 'Machine Position'),
            (self.playerHouseInformationLabel, self.machineHouseInformationLabel)
        ]
        self.tbHouse = gui.Table.new_from_list(content=self.tableHouseInformation,width='500px',height='100px',margin='10px')

        #Build up the gui
        main_container.append(self.lbl,'lbl')
        main_container.append(self.bt1,'btn1')
        main_container.append(self.tbl,'tb1')
        main_container.append(self.tbHouse, 'tbHouse')
        
        # returning the root widget
        return main_container
    
    def rollDice(self, widget, *args, **kwargs):
        self.board.playerMovement()

        playerHouseInformation = self.board.getPrettyInformation(self.board.player)
        machineHouseInformation = self.board.getPrettyInformation(self.board.machine)

        # Refesh User's Labels
        self.playerCurrentPositonLabel.set_text(f'{self.board.player.getCurrentPosition()}')
        self.playerCycleNumberLabel.set_text(f'{self.board.player.getCycleNumber()}')
        self.playerCurrentMoneyLabel.set_text(f'B {self.board.player.money}')
        self.playerHouseInformationLabel.set_text(playerHouseInformation)
        
        # Refesh User's Machine
        self.machineCurrentPositonLabel.set_text(f'{self.board.machine.getCurrentPosition()}')
        self.machineCycleNumberLabel.set_text(f'{self.board.machine.getCycleNumber()}')
        self.machineCurrentMoneyLabel.set_text(f'B {self.board.machine.money}')
        self.machineHouseInformationLabel.set_text(machineHouseInformation)
        
        return True


if __name__ == "__main__":
    # starts the webserver
    start(MyApp, address='127.0.0.1', port=8081, start_browser=False)

