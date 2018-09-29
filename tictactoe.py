from kivy.app import App

from kivy.config import Config

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TicTacToeApp(App):
    title = 'Tic Tac Toe'
    board = []
    choice = ['X', 'O']
    switch = 0 #มีไว้เพื่อ เลือก x,o
    cols = rows = 3
    count_xo = 0 #มีไว้สำหรับเช็ค ช่องในตาราง เพื่อทำเงื่อนไขเสมอกัน

    def build(self):
        Config.set('graphics', 'width', '450') 
        Config.set('graphics', 'height', '450') # ตั้งค่าขนาดหน้าต่าง
        Config.set('graphics','resizable', False) # ตั้งค่าไม่ให้สามารถย่อหรือขยายหน้าต่างได้
        
        root = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = self.cols, rows = self.rows, spacing = 5)
        self.board = [[None for col in range(self.cols)] for row in range(self.rows)]# สร้าง list เก็บค่าตารางเป็นแบบเมทริกต์
        print(self.board)
        for row in range(self.rows):
            for col in range(self.cols):
                bt = Button(
                        text = '',
                        font_size = 200,
                        disabled = False, # ทำให้ปุ่มสามารถกดได้
                        on_press = self.on_press #เมื่อกดปุ่ม จะไปทำงาน method on_press
                    )
                self.board[row][col] = bt # นำ ปุ่มไปเก็บไว้ใน ตารางที่สร้างขึ้น
                grid.add_widget(bt) # เพิ่ม ปุ่มแต่ละอันซึ่งอยู่ภายใต้ grid
        
        self.label = Label(
                text="Player "+ self.choice[self.switch] + " choose",
                color = (0, 1, 1, 1),
                size_hint = [1,.15]) # ข้อความแสดงการกระทำต่างๆ

        root.add_widget(self.label)  #ทำการนำ Label มาไว้ใน BoxLayout
        root.add_widget(grid) #ทำการนำ grid ที่ภายในเป็นช่อง(ปุ่ม) 9 ช่อง มาไว้ใน BoxLayout ถัดจาก Label
        root.add_widget(  # นำปุ่ม restart มาใส่ไว้ใน BoxLayout ถัดจาก grid
            Button(
                text = "Restart",
                size_hint = [1,.15],
                on_press = self.restart
            ) # เพิ่มปุ่ม restart ไว้เริ่มเล่นเกมใหม่อีกครั้ง
            )
        return root

    def on_press(self, bt):  
        bt.disabled = True # ทำให้หลังจากกดปุ่มแล้ว ไม่สามารถกดปุ่มได้อีก
        bt.text = self.choice[self.switch] # ใส้ x,o ลงในช่องที่เลือก
        self.count_xo += 1

        if self.switch != 0:
            self.switch = 0 # switch ไปเป็น X
        else: 
            self.switch = 1 # switch ไปเป็น O

        self.label.text = "Player "+ self.choice[self.switch] + " choose"

        win_pattern = [
            [0,1,2],[3,4,5],[6,7,8], # Horizontal
            [0,3,6],[1,4,7],[2,5,8], # Vertical
            [0,4,5],[2,4,6]          # Diagonal
        ]

        win = False

        # val = [[col.text for col in row] for row in self.board]
        
        check_pattern = [
            [self.board[0][col].text for col in range(self.cols)], #[0,1,2]
            [self.board[1][col].text for col in range(self.cols)], #[3,4,5]
            [self.board[2][col].text for col in range(self.cols)], #[6,7,8]

            [self.board[y][0].text for y in range(self.rows)], #[0,3,6]
            [self.board[y][1].text for y in range(self.rows)], #[1,4,7]
            [self.board[y][2].text for y in range(self.rows)], #[2,5,8]

            [self.board[0][0].text, self.board[1][1].text, self.board[2][2].text], #[0,4,5]
            [self.board[0][2].text, self.board[1][1].text, self.board[2][0].text] #[2,4,6]
            

        ]
        print(check_pattern)

        if self.count_xo == 9:
            self.label.text = "Draw" #เมื่อ ช่องทุกช่องเต็มหมดแล้ว ให้ขึ้นข้อความ Draw

        for i in range(8):
            if check_pattern[i].count('X') == 3: # เมื่อมี X เรียงกัน 3 ตัว ที่อยู่ในแต่ละเงื่อนไข จาก check_pattern
                win = True 
                self.label.text = "Player X Win" # แสดงข้อความ
            elif check_pattern[i].count('O') == 3: # เมื่อมี O เรียงกัน 3 ตัว ที่อยู่ในแต่ละเงื่อนไข จาก check_pattern
                win = True
                self.label.text = "Player O Win" # แสดงข้อความ

        if win:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.board[row][col].disabled = True    

    def restart(self, bt):
        global switch, count_xo;
        self.count_xo = 0 # reset ให้กลับไปเป็นค่าเริ่มต้น
        self.switch = 0 # reset ให้กลับไปเป็นค่าเริ่มต้น
        self.label.text = "Player "+ self.choice[self.switch] + " choose" # reset ให้กลับไปเป็นค่าเริ่มต้น
        print(self.switch)
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col].disabled = False
                self.board[row][col].text = '' # resetตาราง แล้วให้สามารถเลือกช่องใส่ x,o ได้
        

if __name__ == '__main__':
    TicTacToeApp().run()