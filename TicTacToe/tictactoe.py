# -*- coding: utf-8 -*-

from myarray2d import Array2D

class TicTacToe:
    
    BLACK = True
    WHITE = False
    EMPTY = None
    
    BLACKWIN = 1
    WHITEWIN = -1
    DRAW = 0
    
    def __init__(self):
        self.board = Array2D(4,4)
        self.player = TicTacToe.BLACK
        self.black = []
        self.white = []
        
        self.magic = Array2D(4,4)
        self.magic[0, 0] = 1
        self.magic[0, 1] = 15
        self.magic[0, 2] = 14
        self.magic[0, 3] = 4

        self.magic[1, 0] = 12
        self.magic[1, 1] = 6
        self.magic[1, 2] = 7
        self.magic[1, 3] = 9

        self.magic[2, 0] = 8
        self.magic[2, 1] = 10
        self.magic[2, 2] = 11
        self.magic[2, 3] = 5

        self.magic[3, 0] = 13
        self.magic[3, 1] = 3
        self.magic[3, 2] = 2
        self.magic[3, 3] = 16
        
    def reset(self):
        self.board.clear(None)
        self.player = TicTacToe.BLACK
        self.black = []
        self.white = []
        
    def clone(self):
        newttt = TicTacToe()
        for row in range(4):
            for col in range(4):
                newttt.board[row, col] = self.board[row, col]
        newttt.player = self.player
        newttt.black = self.black[:]
        newttt.white = self.white[:]
        
        return newttt
    
    def ToString(self):
        l = []
        for row in range(4):
            for col in range(4):
                if self.board[row, col] == TicTacToe.BLACK:
                    l.append('X')
                elif self.board[row, col] == TicTacToe.WHITE:
                    l.append('O')
                else:
                    l.append('_')
        return ''.join(l)
    
    def print(self):
        for row in range(4):
            for col in range(4):
                if self.board[row, col] == TicTacToe.BLACK:
                    print('X', end=' ')
                elif self.board[row, col] == TicTacToe.WHITE:
                    print('O', end=' ')
                else:
                    print('_', end=' ')
            print()
    
    def play(self, row, col):
        self.board[row, col] = self.player
        if self.player == TicTacToe.BLACK:
            self.black.append(self.magic[row, col])
        else:
            self.white.append(self.magic[row, col])
        self.player = not self.player
        
    def getPlayer(self):
        return self.player
    
    def getAllMoves(self):
        return [(row, col) for row in range(4) \
                               for col in range(4) \
                                   if self.board[row, col] == TicTacToe.EMPTY]
    
    def isWin(self, n, goal, moves):
        moves_clone = moves[:]
        if n == 0:
            return goal == 0
        elif goal <= 0:
            return False
        elif len(moves_clone) == 0:
            return False
        else:
            item = moves_clone.pop(0)
            if self.isWin(n-1, goal-item, moves_clone[:]):
                return True
            elif self.isWin(n, goal, moves_clone[:]):
                return True
        return False
    
    def isGameOver(self):
        if self.isWin(4, 34, self.black):
            return TicTacToe.BLACKWIN
        elif self.isWin(4, 34, self.white):
            return TicTacToe.WHITEWIN
        elif len(self.black)+len(self.white) == 16:
            return TicTacToe.DRAW
        else:
            return None


def main():
    ttt = TicTacToe()
    ttt.play(1, 1)
    ttt.play(0, 0)
    ttt.play(2, 0)
    ttt.play(0, 1)
    ttt.play(0, 2)
    ttt.print()
    print(ttt.isGameOver())
    print(ttt.ToString())
    
if __name__ == '__main__':
    main()