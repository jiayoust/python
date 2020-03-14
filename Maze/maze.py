# -*- coding: utf-8 -*-
from random import *
from myarray2d import Array2D

class Maze:
    HEIGHT = 20
    WIDTH = 20
    GOAL = Array2D(HEIGHT, WIDTH)
    EMPTY = 0
    OBSTACLE = -1
    OCCUPIED = 1
    def __init__(self, height, width):
        seed()
        self.maze = Array2D(height, width)
        self.start = (0, 0)
        self.goal = (height-1, width-1)
        self.maze.clear(Maze.EMPTY)
        for count in range(int(height*width*0.1)):
            row = int(random()*100 % height)
            col = int(random()*100 % width)
            if (row, col) == self.start or (row, col) == self.goal:
                continue
            self.maze[row, col] = Maze.OBSTACLE
            
    def __getitem__(self, ndxTuple):
        return self.maze.__getitem__(ndxTuple)

    def _calcHeuristics(self):
        heuristics = 0
        for row in range(Maze.HEIGHT):
            for col in range(Maze.WIDTH):
                item = self[row, col]
                if item != ' ':
                    index = Maze.ITEMS.index(item)
                    row1 = index // Maze.WIDTH
                    col1 = index % Maze.WIDTH
                    heuristics += abs(row1 - row) + abs(col1 - col)
        return heuristics

    def __setitem__(self, ndxTuple, value):
        self.maze.__setitem__(ndxTuple, value)
        
    def getAllMoves(self, row, col):
        width = self.numCols()
        height = self.numRows()
        moves = []
        offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for x, y in offsets:
            x = col + x
            y = row + y
            if x < 0 or x > width-1 or \
               y < 0 or y > height-1:
                continue
            if self.maze[y, x] != Maze.OBSTACLE:
                moves.append((y, x))
        return moves

    def isGoal(self):
        for row in range(Maze.HEIGHT):
            for col in range(Maze.WIDTH):
                if self[row, col] != Maze.GOAL[row, col]:
                    return False
        return True

    def __lt__(self, other):  # for PriorityQueue
        return self.heuristics < other.heuristics

    def numRows(self):
        return self.maze.numRows()
    def ToString(self):
        items = [self[row, col] for row in range(Maze.HEIGHT) \
                                    for col in range(Maze.WIDTH)]
        return items
    def numCols(self):
        return self.maze.numCols()

    def cost(self):
        return self.__cost_so_far
    def print(self):
        rows = self.numRows()
        cols = self.numCols()
        for row in range(rows):
            for col in range(cols):
                if self.maze[row, col] == Maze.EMPTY:
                    print('_', end=' ')
                elif self.maze[row, col] == Maze.OBSTACLE:
                    print('|', end=' ')
                else:
                    print('O', end=' ')
            print()
                    
def main():
    maze = Maze(20, 20)
    maze.print()
    print()
    print(maze.getAllMoves(3, 3))
    
if __name__ == '__main__':
    main()