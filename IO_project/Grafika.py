import tkinter as tk
from tkinter import messagebox

class Widok(tk.Frame):
    def __init__(self):
        self.__mainWindow = tk.Tk()
        self.__mainWindow.resizable(False, False)
        super().__init__(self.__mainWindow)
        self.__manager = None

        # wczytanie grafik do programu
        self.__pionekb = tk.PhotoImage(file="pionekb.gif")
        self.__damab = tk.PhotoImage(file="damab.gif")
        self.__pionekbz = tk.PhotoImage(file="pionekbz.gif")
        self.__damabz = tk.PhotoImage(file="damabz.gif")
        self.__pionekc = tk.PhotoImage(file="pionekc.gif")
        self.__damac = tk.PhotoImage(file="damac.gif")
        self.__pionekcz = tk.PhotoImage(file="pionekcz.gif")
        self.__damacz = tk.PhotoImage(file="damacz.gif")
        self.__polec = tk.PhotoImage(file="kratkac.gif")
        self.__poleb = tk.PhotoImage(file="kratkab.gif")

        self.__tura = None
        self.__koniecGry = None
        self.__test = None
        self.__buttons = None
        self.__clicked_button = None


    def utworz_okno(self, width=540, height=480, title='PROJEKT WARCABY'):
        self.__mainWindow.geometry('{}x{}'.format(width, height))
        self.winfo_toplevel().title(title)

    def utworz_plansze(self, board, n):
        self.pack()
        self.obiekty_graficzne(board, n)

    def obiekty_graficzne(self, board, n):
        self.__buttons = [[0 for i in range(n)] for i in range(n)]
        for x in range(0, n, 1):
            for y in range(0, n, 1):
                tmp = board[x][y]
                img = self.wybierz_obrazek(tmp.text)
                self.__buttons[x][y] = tk.Button(self, text=tmp.text, command=lambda row=tmp.row, column=tmp.column: self.clicked(row, column), bg=tmp.bg, fg=tmp.fg, image=img, compound='none')
                buf = self.__buttons[x][y]
                buf.grid(row=tmp.row, column=tmp.column)

        rightFrame = tk.Frame(self.__mainWindow)
        rightFrame.pack(side='right', anchor='ne')

        self.__odNowa = tk.Button(rightFrame, text="Zacznij gre od nowa", command=self.__manager.od_nowa, font=(None, 28))
        self.__odNowa.grid(row=1, column=5)
        self.__test = tk.Button(rightFrame, text="TESTY", command=lambda n=4: self.__manager.clicked_test(n), font=(None, 28))
        self.__test.grid(row=1, column=6)
        self.__tura = tk.Label(self, text="Tura gracza 1", fg="blue", font=(None , 12))
        self.__tura.grid(row=0, column=8)


    def start_loop(self):
        self.mainloop()

    def add_manager(self, manager):
        self.__manager = manager

    def clicked(self, r, c):
        self.__manager.clicked(r, c)

    def wybierz_obrazek(self, nazwa):
        if nazwa == 'czarne':
            return self.__polec
        elif nazwa == 'biale':
            return self.__poleb
        elif nazwa == 'Pb':
            return self.__pionekb
        elif nazwa == 'Pc':
            return self.__pionekc
        elif nazwa == 'zPbz':
            return self.__pionekbz
        elif nazwa == 'zPcz':
            return self.__pionekcz
        elif nazwa == 'PbD':
            return self.__damab
        elif nazwa == 'PcD':
            return self.__damac
        elif nazwa == 'zPbDz':
            return self.__damabz
        elif nazwa == 'zPcDz':
            return self.__damacz


    def update_button(self, tmp):
        img = self.wybierz_obrazek(tmp.text)
        self.__buttons[tmp.row][tmp.column].destroy()
        self.__buttons[tmp.row][tmp.column] = tk.Button(self, text=tmp.text, command=lambda row=tmp.row, column=tmp.column: self.clicked(row, column), bg=tmp.bg, fg=tmp.fg, image=img, compound='none')
        buf = self.__buttons[tmp.row][tmp.column]
        buf.grid(row=tmp.row, column=tmp.column)
        buf.update()

    def pokaz_komunikat(self, komunikat):
        messagebox.showinfo("", komunikat)

    def zmiana_tury(self):
        if self.__tura['text'] == 'Tura gracza 1':
            self.__tura.config(text='Tura gracza 2')
        else:
            self.__tura.config(text='Tura gracza 1')


    def reset_planszy(self, board, n):
        for x in self.__buttons:
            for y in x:
                y.destroy()
        for x in range(0, n, 1):
            for y in range(0, n, 1):
                tmp = board[x][y]
                img = self.wybierz_obrazek(tmp.text)
                self.__buttons[x][y] = tk.Button(self, text=tmp.text, command=lambda row=tmp.row, column=tmp.column: self.clicked(row, column), bg=tmp.bg, fg=tmp.fg, image=img, compound='none')
                buf = self.__buttons[x][y]
                buf.grid(row=tmp.row, column=tmp.column)
        self.__tura.destroy()
        self.__tura = tk.Label(self, text="Tura gracza 1", fg="blue", height=1, width=12, font=(None , 12))
        self.__tura.grid(row=0, column=8)