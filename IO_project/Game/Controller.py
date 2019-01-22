class Controller:
    def __init__(self, widok, rozgrywka):
        self.__widok = widok
        self.__rozgrywka = rozgrywka

## funkcja rozpoczynajaca gre
## tworzy plansze

    def reset(self):
        board = self.__rozgrywka.utworz_plansze()
        self.__widok.reset_planszy(board, n=8)

    def od_nowa(self):
        board = self.__rozgrywka.utworz_plansze()
        self.__widok.reset_planszy(board, n=8)
        self.__rozgrywka.od_nowa()

    def clicked(self, r, c):
        self.__rozgrywka.select_button(r, c)

    def update_button(self, pionek):
        self.__widok.update_button(pionek)

    def komunikat(self, m):
        self.__widok.pokaz_komunikat(m)

    def zmiana_tury(self):
        self.__widok.zmiana_tury()

