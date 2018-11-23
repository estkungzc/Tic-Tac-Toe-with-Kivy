from kivy.app import App

from kivy.config import Config

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TicTacToeApp(App):
    title = 'Tic Tac Toe'
    board = []
    choice = ['X', 'O']
    switch = 0  # มีไว้เพื่อ เลือก x,o
    cols = rows = 3
    count_xo = 0  # มีไว้สำหรับเช็ค ช่องในตาราง เพื่อทำเงื่อนไขเสมอกัน
    win = False
    label = Label()
    textInput = TextInput()

    def build(self):
        # ตั้งค่าขนาดหน้าต่าง
        Config.set('graphics', 'width', '450')
        Config.set('graphics', 'height', '450')
        # ตั้งค่าไม่ให้สามารถย่อหรือขยายหน้าต่างได้
        Config.set('graphics', 'resizable', False)

        root = BoxLayout(orientation="vertical")
        grid = GridLayout(cols=self.cols, rows=self.rows, spacing=5)
    
        pushButton = Button(text='Selected')
        pushButton.bind(
            on_press = self.on_selected
        )
        # pushButton.bind(on_release=self.on_press(textInput.entry.text))

        inputGridLayout = GridLayout(
            cols=2, rows=1, spacing=5, size_hint_y=None)
        inputGridLayout.add_widget(self.textInput)
        inputGridLayout.add_widget(pushButton)
        root.add_widget(inputGridLayout)
        self.board = [[None for col in range(self.cols)] for row in range(
            self.rows)]  # สร้างตารางซึ่งเป็น array 2 มิติ สำหรับเก็บ x,o ไว้
        # print(self.board)
        for row in range(self.rows):
            for col in range(self.cols):
                bt = Button(
                    text='',
                    font_size=150,
                    disabled=False  # ทำให้ปุ่มสามารถกดได้
                    # on_press=self.on_press  # เมื่อกดปุ่ม จะไปทำงาน method on_press
                )
                # นำ ปุ่มไปเก็บไว้ใน ตารางที่สร้างขึ้น
                self.board[row][col] = bt
                grid.add_widget(bt)  # เพิ่ม ปุ่มแต่ละอันซึ่งอยู่ภายใต้ grid

        self.label = Label(
            text="Player {} choose".format(self.choice[self.switch]),
            color=(0, 1, 1, 1),
            size_hint=[1, .15])  # ข้อความแสดงการกระทำต่างๆ

        root.add_widget(self.label)  # ทำการนำ Label มาไว้ใน BoxLayout
        # ทำการนำ grid ที่ภายในเป็นช่อง(ปุ่ม) 9 ช่อง มาไว้ใน BoxLayout ถัดจาก Label
        root.add_widget(grid)
        root.add_widget(  # นำปุ่ม restart มาใส่ไว้ใน BoxLayout ถัดจาก grid
            Button(
                text="Restart",
                size_hint=[1, .15],
                on_press=self.restart
            )  # เพิ่มปุ่ม restart ไว้เริ่มเล่นเกมใหม่อีกครั้ง
        )
        return root

    def on_selected(self,bt):
        
        if self.textInput.text == '1':
            self.board[0][0].disabled = True
            self.board[0][0].text = self.choice[self.switch]
        elif self.textInput.text == '2':
            self.board[0][1].disabled = True
            self.board[0][1].text = self.choice[self.switch]
        elif self.textInput.text == '3':
            self.board[0][2].disabled = True
            self.board[0][2].text = self.choice[self.switch]
        elif self.textInput.text == '4':
            self.board[1][0].disabled = True
            self.board[1][0].text = self.choice[self.switch]
        elif self.textInput.text == '5':
            self.board[1][1].disabled = True
            self.board[1][1].text = self.choice[self.switch]
        elif self.textInput.text == '6':
            self.board[1][2].disabled = True
            self.board[1][2].text = self.choice[self.switch]
        elif self.textInput.text == '7':
            self.board[2][0].disabled = True
            self.board[2][0].text = self.choice[self.switch]
        elif self.textInput.text == '8':
            self.board[2][1].disabled = True
            self.board[2][1].text = self.choice[self.switch]
        elif self.textInput.text == '9':
            self.board[2][2].disabled = True
            self.board[2][2].text = self.choice[self.switch]
        self.count_xo += 1

        if self.switch != 0:
            self.switch = 0  # switch ไปเป็น X
        else:
            self.switch = 1  # switch ไปเป็น O
        # แสดงข้อความว่าถึงตาใคร
        self.message(self.choice[self.switch])

        if self.count_xo >= 3:
            self.game_check()

    def game_check(self):
        val = [[col.text for col in row]
               for row in self.board]  # get x,o value from board

        for c in self.choice:
            pattern = [c for _ in range(self.rows)]

            # horizontal check
            for row in val:
                if row == pattern:
                    self.you_win()
                    return self.message(c)

            # vertical check
            for col in range(self.cols):
                if [row[col] for row in val] == pattern:
                    self.you_win()
                    return self.message(c)
            #if [row[i] for i,row in zip(range(self.cols-1,-1,-1),val)] == [c for row in range(self.rows)]:
            #     self.you_win()
            #     return self.message(c)

            # forward diagonal check
            if [row[index] for index, row in enumerate(val)] == pattern:
                self.you_win()
                return self.message(c)

            # backward diagonal check
            elif [row[-index] for index, row in enumerate(val, 1)] == pattern:
                self.you_win()
                return self.message(c)

        # draw check
        if self.count_xo == self.rows*self.cols:
            return self.message()

    def message(self, who=None):
        if self.win:  # แสดงข้อความผู้ชนะ
            self.label.text = "Player {} Win".format(who)
        elif self.count_xo == self.rows * self.cols:  # แสดงข้อความเสมอ
            self.label.text = "Draw"
        else:  # แสดงข้อความว่าถึงตาใคร
            self.label.text = "Player {} choose".format(who)

    def you_win(self):
        global win
        self.win = True
        #ทำให้ไม่สามารถใส่x,oในตารางได้
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col].disabled = True

    def restart(self, bt):
        global switch, count_xo, win
        self.count_xo = 0  # reset ให้กลับไปเป็นค่าเริ่มต้น
        self.switch = 0  # reset ให้กลับไปเป็นค่าเริ่มต้น
        self.win = False
        # reset ให้กลับไปเป็นค่าเริ่มต้น
        self.label.text = "Player " + self.choice[self.switch] + " choose"

        # resetตาราง แล้วให้สามารถเลือกช่องใส่ x,o ได้
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col].disabled = False
                self.board[row][col].text = ''


if __name__ == '__main__':
    TicTacToeApp().run()
