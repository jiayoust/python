# -*- coding: utf-8 -*-

from graphics import *
from tictactoe import *

class TTTInput:
    def __init__(self, win):
        self.win = win
        
    def input(self, ttt):
        mpos = self.win.checkMouse()
        if mpos == None:
            return False
        moves = ttt.getAllMoves()
        row, col = 5-int(mpos.getY())-1, int(mpos.getX())-1
        if (row, col) not in moves:
            return False
        ttt.play(row, col)
        return True