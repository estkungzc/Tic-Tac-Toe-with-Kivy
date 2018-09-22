from kivy.app import App

from kivy.config import Config

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class TicTacToeApp(App):
    title = 'Tic Tac Toe'
    table = []
    choice = ['X', 'O']
    switch = 0
    

    def build(self):
        Config.set('graphics', 'width', '450')
        Config.set('graphics', 'height', '450')
        Config.set('graphics','resizable', False)
        
        root = BoxLayout(orientation = "vertical")

        grid = GridLayout(cols = 3, rows = 3, spacing = 5)

        for i in range(9):
            bt = Button(
                    text = '',
                    font_size = 200,
                    on_press = self.let_start
                )
            self.table.append(bt)
            grid.add_widget(bt)
        root.add_widget(grid)
        return root

    def let_start(self, bt):
        if bt.text != ('X' or 'O'):
            bt.text = self.choice[self.switch]
            if self.switch != 0 : self.switch = 0
            else: self.switch = 1

if __name__ == '__main__':
    TicTacToeApp().run()