class PustePole():
    def __init__(self, text="", bg="black", fg="white", row=0, column=0, height=4, width=8):
        self.text = text
        self.row = row
        self.column = column
        self.bg = bg
        self.fg = fg
        self.height = height
        self.width = width

class Pionek(PustePole):
    def __init__(self, text="", bg="black", fg="white", row=0, column=0, height=4, width=8, player=1):
        super().__init__(text, bg, fg, row, column, height, width)
        self.__beating = False
        self.player = player
    mabicie1 = False
    mabicie2 = False

    def ktobicie(tura):
        if tura is 1 and Pionek.mabicie1 is True:
            return True
        elif tura is 2 and Pionek.mabicie2 is True:
            return True
        else:
            return False

    def jest_bicie(self):
        self.__beating = True

    def niejest_bicie(self):
        self.__beating = False

    def beating(self):
        return self.__beating

    def czy_ruch(self, clicked, board):
        return None

    def czy_bicie(self, clicked, board):
        return None

class ZwyklyPionek(Pionek):
    def __init__(self, text="Pb", bg="black", fg="white", row=0, column=0, height=4, width=8, player=1):
        super().__init__(text, bg, fg, row, column, height, width, player)

    def czy_ruch(self, clicked, board):
        #srawdzamy czy nasz pionek moze sie ruszyc w dane klikniete miejsce badajac rundę
        if type(clicked) is PustePole:
            if self.player is 1:
                if clicked.row - self.row is 1 and abs(self.column - clicked.column) is 1:
                    return True
                else:
                    return False
            elif self.player is 2:
                if self.row - clicked.row is 1 and abs(self.column - clicked.column) is 1:
                    return True
                else:
                    return False
        else:
            return False

    def czy_bicie(self, clicked, board):
        r = int((self.row+clicked.row)/2)
        c = int((self.column+clicked.column)/2)
        beated = board[r][c]
        if type(clicked) is PustePole and type(beated) is not PustePole and beated.player is not self.player:
            if abs(self.row-clicked.row) is 2 and abs(self.column-clicked.column) is 2:
                return True
        else:
            return False
        #badamy czy pionek moze zbic pionka przeskakujac na pole clicked

    def szukaj_bicia(self, board, n):
        r = self.row
        c = self.column
        flag = 0
        if r + 2 < n and c + 2 < n:  # prawo dół
            if self.czy_bicie(board[r + 2][c + 2], board):
                self.jest_bicie()
                flag = 1
        if r + 2 < n and c - 2 >= 0:  # lewo dół
            if self.czy_bicie(board[r + 2][c - 2], board):
                self.jest_bicie()
                flag = 1
        if r - 2 >= 0 and c + 2 < n:  # prawo góra
            if self.czy_bicie(board[r - 2][c + 2], board):
                self.jest_bicie()
                flag = 1
        if r - 2 >= 0 and c - 2 >= 0:  # lewo góra
            if self.czy_bicie(board[r - 2][c - 2], board):
                self.jest_bicie()
                flag = 1
        if flag is 0:
            self.niejest_bicie()

        if self.beating() is True:
            if self.player is 1:
                Pionek.mabicie1 = True
            else:
                Pionek.mabicie2 = True


class Damka(Pionek):
    def __init__(self, text="PbD", bg="black", fg="white", row=0, column=0, height=4, width=8, player=1):
        super().__init__(text, bg, fg, row, column, height, width, player)

    def czy_ruch(self, clicked, board):
        #srawdzamy czy nasza damka moze sie ruszyc w dane klikniete miejsce badajac rundę
        if type(clicked) is PustePole:
            r = int(self.row - clicked.row)
            c = int(self.column - clicked.column)
            if abs(r) != abs(c): # czy to przekatna!!!
                return False
            if r > 0 and c > 0:
                #gora lewo
                tmprow = self.row - 1
                tmpcolumn = self.column - 1
                while(tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        return False
                    tmprow = tmprow - 1
                    tmpcolumn = tmpcolumn - 1
                return True
            elif r>0 and c < 0:
                #gora prawo
                tmprow = self.row - 1
                tmpcolumn = self.column + 1
                while (tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        return False
                    tmprow = tmprow - 1
                    tmpcolumn = tmpcolumn + 1
                return True
            elif r < 0 and c > 0:
                #dol lewo
                tmprow = self.row + 1
                tmpcolumn = self.column - 1
                while (tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        return False
                    tmprow = tmprow + 1
                    tmpcolumn = tmpcolumn - 1
                return True
            elif r < 0 and c < 0:
                #dol prawo
                tmprow = self.row + 1
                tmpcolumn = self.column + 1
                while (tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        return False
                    tmprow = tmprow + 1
                    tmpcolumn = tmpcolumn + 1
                return True
            else:
                return False
        else:
            return False

    def czy_bicie(self, clicked, board):
        if type(clicked) is PustePole:
            r = int(self.row - clicked.row)
            c = int(self.column - clicked.column)
            counter = 0
            if abs(r) != abs(c):
                return False
            if r > 0 and c > 0:
                #gora lewo
                tmprow = self.row - 1
                tmpcolumn = self.column - 1
                while(tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        if board[tmprow][tmpcolumn].player is self.player:
                            counter = 2
                            break
                        else:
                            counter = counter + 1
                    tmprow = tmprow - 1
                    tmpcolumn = tmpcolumn - 1
            elif r>0 and c < 0:
                #gora prawo
                tmprow = self.row - 1
                tmpcolumn = self.column + 1
                while (tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        if board[tmprow][tmpcolumn].player is self.player:
                            counter = 2
                            break
                        else:
                            counter = counter + 1
                    tmprow = tmprow - 1
                    tmpcolumn = tmpcolumn + 1
            elif r < 0 and c > 0:
                #dol lewo
                tmprow = self.row + 1
                tmpcolumn = self.column - 1
                while (tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        if board[tmprow][tmpcolumn].player is self.player:
                            counter = 2
                            break
                        else:
                            counter = counter + 1
                    tmprow = tmprow + 1
                    tmpcolumn = tmpcolumn - 1
            elif r < 0 and c < 0:
                #dol prawo
                tmprow = self.row + 1
                tmpcolumn = self.column + 1
                while (tmprow != clicked.row and tmpcolumn != clicked.column):
                    if type(board[tmprow][tmpcolumn]) is not PustePole:
                        if board[tmprow][tmpcolumn].player is self.player:
                            counter = 2
                            break
                        else:
                            counter = counter + 1
                    tmprow = tmprow + 1
                    tmpcolumn = tmpcolumn + 1
            else:
                return False
            if counter is not 1:
                return False
            else:
                return True

    def szukaj_bicia(self, board, n):
        r = self.row
        c = self.column
        flag = 0
        if r + 2 < n and c + 2 < n:  # prawo dół
            tmprow = self.row + 1
            tmpcolumn = self.column + 1
            while tmprow < n and tmpcolumn < n:
                if self.czy_bicie(board[tmprow][tmpcolumn], board):
                    self.jest_bicie()
                    flag = 1
                    break
                tmprow = tmprow + 1
                tmpcolumn = tmpcolumn + 1
        if r + 2 < n and c - 2 >= 0:  # lewo dół
            tmprow = self.row + 1
            tmpcolumn = self.column - 1
            while tmprow < n and tmpcolumn >= 0:
                if self.czy_bicie(board[tmprow][tmpcolumn], board):
                    self.jest_bicie()
                    flag = 1
                    break
                tmprow = tmprow + 1
                tmpcolumn = tmpcolumn - 1
        if r - 2 >= 0 and c + 2 < n:  # prawo góra
            tmprow = self.row - 1
            tmpcolumn = self.column + 1
            while tmprow >= 0 and tmpcolumn < n:
                if self.czy_bicie(board[tmprow][tmpcolumn], board):
                    self.jest_bicie()
                    flag = 1
                    break
                tmprow = tmprow - 1
                tmpcolumn = tmpcolumn + 1
        if r - 2 >= 0 and c - 2 >= 0:  # lewo góra
            tmprow = self.row - 1
            tmpcolumn = self.column - 1
            while tmprow >= 0 and tmpcolumn >= 0:
                if self.czy_bicie(board[tmprow][tmpcolumn], board):
                    self.jest_bicie()
                    flag = 1
                    break
                tmprow = tmprow - 1
                tmpcolumn = tmpcolumn - 1
        if flag is 0:
            self.niejest_bicie()
        if self.beating() is True:
            if self.player is 1:
                Pionek.mabicie1 = True
            else:
                Pionek.mabicie2 = True