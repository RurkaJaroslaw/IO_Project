from Game.Pion import *
from Game.Grafika import Widok
from Game.Controller import Controller

class Rozgrywka:
    def __init__(self):
        self.__board = None
        self.__n = 8
        self.__controller = None
        self.__selected_button = None
        self.__turaGracza = 1
        self.__pionki_gracza1 = 12
        self.__pionki_gracza2 = 12
        self.__reset = False

    def add_controller(self, controller):
        self.__controller = controller

    def utworz_plansze(self):
        self.__board = [["bc"[(i + j + self.__n % 2 + 1) % 2] for i in range(self.__n)] for j in range(self.__n)]
        for x in range(0, self.__n, 1):
            for y in range(0, self.__n, 1):
                if x in range(0, 3, 1) and self.__board[x][y] == 'c':
                    self.__board[x][y] = ZwyklyPionek(text='Pb', row=x, column=y, player=1)
                elif x in range(5, 8, 1) and self.__board[x][y] == 'c':
                    self.__board[x][y] = ZwyklyPionek(text='Pc', row=x, column=y, player=2)
                elif self.__board[x][y] == 'c':
                    self.__board[x][y] = PustePole(text='czarne', row=x, column=y)
                else:
                    self.__board[x][y] = PustePole(text='biale', row=x, column=y)
        return self.__board

    def select_button(self, r, c):
        clicked = self.__board[r][c]
        if self.__selected_button is not None and self.__selected_button.row == r and self.__selected_button.column == c:  # odznaczamy
            self.unselect_button()
        elif self.__selected_button is not None:  # zaznaczamy drugie pole
            if Pionek.ktobicie(self.__turaGracza) is False and self.__selected_button.czy_ruch(clicked, self.__board):
                self.move_button(self.__selected_button, clicked)
            elif self.__selected_button.beating() is True:
                if self.__selected_button.czy_bicie(clicked, self.__board):
                    self.ruch(self.__selected_button, clicked)
                else:
                    self.__controller.komunikat('Ruch niedozwolony!')
            else:
                self.__controller.komunikat('Ruch niedozwolony!')
        elif type(clicked) is not PustePole and clicked.player is self.__turaGracza:  # zaznaczamy
            self.select(clicked)
        elif type(clicked) is not PustePole:
            self.__controller.komunikat('Runda przeciwnika!')

    def select(self, pionek):
        self.__selected_button = pionek
        pionek.text = 'z{}z'.format(pionek.text)
        self.__controller.update_button(pionek)

    def unselect_button(self):
        self.__selected_button.text = self.__selected_button.text[1:-1]
        self.__controller.update_button(self.__selected_button)
        self.__selected_button = None

    def move_button(self, pionek, pole):
        self.odwroc_pola(pole, pionek)
        # if pionek jest na ostatnim polu, to zamien w damke
        self.unselect_button()
        self.zamianaDama(pionek)
        self.zmiana_tury()

    def zmiana_tury(self):
        Pionek.mabicie1 = False
        Pionek.mabicie2 = False
        self.po_bicie()  # ustawiamy beating player od nowa
        # nie zmieniamy kiedy mamy kolejne bicie
        if self.__turaGracza is 1:
            self.__turaGracza = 2
        else:
            self.__turaGracza = 1
        self.__controller.zmiana_tury()

    def po_bicie(self):
        for x in self.__board:
            for y in x:
                if type(y) is not PustePole:
                    y.szukaj_bicia(self.__board, self.__n)

    def odwroc_pola(self, current, next):

        row = current.row
        column = current.column

        rownext = next.row
        columnnext = next.column

        next.row = row
        next.column = column

        current.row = rownext
        current.column = columnnext

        tmp = current

        self.__board[row][column] = self.__board[rownext][columnnext]
        self.__board[rownext][columnnext] = tmp
        self.__controller.update_button(current)
        self.__controller.update_button(next)


    def ruch(self, first, second):
        self.unselect_button()
        if type(first) is ZwyklyPionek:
            r = int((first.row + second.row) / 2)
            c = int((first.column + second.column) / 2)
            p = PustePole(text="czarne", row=r, column=c)
            self.__board[r][c] = p
            self.__controller.update_button(p)
        elif type(first) is Damka:
            r = int(first.row - second.row)
            c = int(first.column - second.column)
            p = None
            if r > 0 and c > 0:
                # gora lewo
                tmprow = first.row - 1
                tmpcolumn = first.column - 1
                while tmprow != second.row and tmpcolumn != second.column:
                    if type(self.__board[tmprow][tmpcolumn]) is not PustePole:
                        p = self.__board[tmprow][tmpcolumn]
                        break
                    tmprow = tmprow - 1
                    tmpcolumn = tmpcolumn - 1
            elif r > 0 and c < 0:
                # gora prawo
                tmprow = first.row - 1
                tmpcolumn = first.column + 1
                while tmprow != second.row and tmpcolumn != second.column:
                    if type(self.__board[tmprow][tmpcolumn]) is not PustePole:
                        p = self.__board[tmprow][tmpcolumn]
                        break
                    tmprow = tmprow - 1
                    tmpcolumn = tmpcolumn + 1
            elif r < 0 and c > 0:
                # dol lewo
                tmprow = first.row + 1
                tmpcolumn = first.column - 1
                while tmprow != second.row and tmpcolumn != second.column:
                    if type(self.__board[tmprow][tmpcolumn]) is not PustePole:
                        p = self.__board[tmprow][tmpcolumn]
                        break
                    tmprow = tmprow + 1
                    tmpcolumn = tmpcolumn - 1
            elif r < 0 and c < 0:
                # dol prawo
                tmprow = first.row + 1
                tmpcolumn = first.column + 1
                while tmprow != second.row and tmpcolumn != second.column:
                    if type(self.__board[tmprow][tmpcolumn]) is not PustePole:
                        p = self.__board[tmprow][tmpcolumn]
                        break
                    tmprow = tmprow + 1
                    tmpcolumn = tmpcolumn + 1
            p = PustePole(text="czarne", row=p.row, column=p.column)
            self.__board[p.row][p.column] = p
            self.__controller.update_button(p)
        self.odwroc_pola(first, second)
        if self.__turaGracza is 1:
            self.__pionki_gracza2 -= 1
        else:
            self.__pionki_gracza1 -= 1
        if self.__pionki_gracza1 is 0:
            self.__controller.komunikat("Wygral gracz 2")
            self.reset_gry()
        if self.__pionki_gracza2 is 0:
            self.__controller.komunikat("Wygral gracz 1")
            self.reset_gry()

        # if runda bedzie sie zmieniac - czyli nie ma juz bicia
        if self.multiple_beating(first) is False:
            if self.__reset is False:
                self.zamianaDama(first)
                self.zmiana_tury()
        else:
            self.select(first)
        self.__reset = False



    def zamianaDama(self, pionek):
        if self.__turaGracza is 1:
            if pionek.row is self.__n - 1:
                d = Damka(text="PbD", row=pionek.row, column=pionek.column, player=1)
                self.__board[pionek.row][pionek.column] = d
                self.__controller.update_button(d)
        elif self.__turaGracza is 2:
            if pionek.row is 0:
                d = Damka(text="PcD", row=pionek.row, column=pionek.column, player=2)
                self.__board[pionek.row][pionek.column] = d
                self.__controller.update_button(d)

    def multiple_beating(self, first):
        first.szukaj_bicia(self.__board, self.__n)
        if first.beating() is True:
            return True
        else:
            return False


    def reset_gry(self):  #zwykly reset gry
        if self.__selected_button is not None:
            self.__selected_button = None
        self.__turaGracza = 1
        self.__pionki_gracza1 = 12
        self.__pionki_gracza2 = 12
        self.__controller.reset()
        self.__reset = True
        Pionek.mabicie1 = False
        Pionek.mabicie2 = False

    def od_nowa(self):  # funkcja zacznij od nowa
        if self.__selected_button is not None:
            self.__selected_button = None
        self.__turaGracza = 1
        self.__pionki_gracza1 = 12
        self.__pionki_gracza2 = 12
        Pionek.mabicie1 = False
        Pionek.mabicie2 = False


class Game:
    def __init__(self):
        self.__widok = Widok()
        self.__rozgrywka = Rozgrywka()
        self.__controller = Controller(self.__widok, self.__rozgrywka)
        self.__widok.add_controller(self.__controller)
        self.__rozgrywka.add_controller(self.__controller)

    def start(self):
        board = self.__rozgrywka.utworz_plansze()
        self.__widok.utworz_okno()
        self.__widok.obiekty_graficzne(board, n=8)
        self.__widok.start_loop()


game = Game()
game.start()
