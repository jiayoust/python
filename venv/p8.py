# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:37:54 2018

@author: duxiaoqin
Functions:
    (1)Puzzle8 class;
"""

from random import *
from myarray2d import Array2D


class Puzzle8:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.puzzle8 = Array2D(self.height, self.width)
        items = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
        for row in range(self.height):
            for col in range(self.width):
                index = randint(0, len(items) - 1)
                item = items[index]
                self[row, col] = item
                if item == ' ':
                    self.space = (row, col)
                items.remove(item)

    def move(self, row, col):
        self[self.space[0], self.space[1]] = self[row, col]
        self[row, col] = ' '
        self.space = (row, col)

    def getStatus(Array2D):
            y = 0;
            for i in xrange(0, 3):
                for j in xrange(0, 3):
                    for m in xrange(0, i + 1):
                        for n in xrange(0, j):
                            if array2d[i][j] > array2d[m][n]:
                                y += 1;
                                return y;


    def __getitem__(self, ndxTuple):
        return self.puzzle8.__getitem__(ndxTuple)

    def __setitem__(self, ndxTuple, value):
        self.puzzle8.__setitem__(ndxTuple, value)

    def numRows(self):
        return self.puzzle8.numRows()

    def numCols(self):
        return self.puzzle8.numCols()

    def getAllMoves(self):
        row = self.space[0]
        col = self.space[1]
        moves = []
        offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for x, y in offsets:
            x = col + x
            y = row + y
            if x < 0 or x > self.width - 1 or \
                    y < 0 or y > self.height - 1:
                continue
            moves.append((y, x))
        return moves


    def ToString(self):
        items = [self[row, col] for row in range(self.height) \
                 for col in range(self.width)]
        return ''.join(items)

    def print(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self[row, col], end=' ')
            print()


def main():
    seed()
    puzzle8 = Puzzle8()
    puzzle8.print()
    print(puzzle8.ToString())
    for i in range(3):
        moves = puzzle8.getAllMoves()
        print(moves)
        puzzle8.move(*moves[0])
        puzzle8.print()
        print(puzzle8.ToString())


if __name__ == '__main__':
    main()