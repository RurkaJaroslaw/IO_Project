import unittest
from Game.Pion import *
from Game.Rozgrywka import *
from Game.Grafika import *
from Game.Controller import *

class Test(unittest.TestCase):
    def TestKtoBicie(self):
        self.AssertEqual(Pionek.ktobicie(1), True)
        self.AssertEqual(Pionek.ktobicie(2), True)
        self.AssertEqual(Pionek.ktobicie(6), False)



