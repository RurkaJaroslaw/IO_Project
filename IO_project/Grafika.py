import tkinter as tk
from tkinter import messagebox

class Widok(tk.Frame):
    def __init__(self):
        self.__mainWindow = tk.Tk()
        self.__mainWindow.resizable(False, False)

        super().__init__(self.__mainWindow)
        self.__manager = None

        self.__przyciski = None
        self.wybrany_przycisk = None

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