# -*- coding: utf-8 -*-


import queue
from myarray2d import Array2D
from mazedraw import *
from priorityqueue import *
from random import *
import math

start=(0,0)
class Maze:
    HEIGHT = 20
    WIDTH = 20
    GOAL = Array2D(HEIGHT, WIDTH)
    EMPTY = 0
    OBSTACLE = -1
    OCCUPIED = 1
    start = (0, 0)
    came_from={}
    def __init__(self, width, height):
        seed()
        self.maze = Array2D(width, height)
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.maze.clear(Maze.EMPTY)
        
        for count in range(int(width*height*0.1)):
            row = int(random()*100 % height)
            col = int(random()*100 % width)
            if (row, col) == self.start or (row, col) == self.goal:
                continue
            self.maze[row, col] = Maze.OBSTACLE
            
    def __getitem__(self, ndxTuple):
        return self.maze.__getitem__(ndxTuple)
    
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
            if self.maze[y, x] == Maze.EMPTY:
                moves.append((y, x))
        return moves
        
    def numRows(self):
        return self.maze.numRows()
    
    def numCols(self):
        return self.maze.numCols()

    def dfs(x,y,step):
        x=0
        y=0
        step=0
        
        
        
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

    def AStar(maze,v,came_from):
        frontier = PriorityQueue()
        goal=(19,19)
        frontier.enqueue(v,0)
        came_from[v]=None
        cost_so_far={}
        cost_so_far[v]=0
        while not frontier.is_empty():
            v=frontier.dequeue()
            if(maze[v[0],v[1]]==Maze.EMPTY):
                if v[0]==maze.goal[0]&v[1]==maze.goal[1]:
                    return v
                else:
                    maze[v[0],v[1]]=Maze.OCCUPIED;
                    moves=[]
                    moves=maze.getAllMoves(v[0],v[1])
                    newcost=cost_so_far[v]+1
                    for w in moves:
                        #if(maze[w[0],w[1]]==0):
                            if(w not in cost_so_far or newcost<cost_so_far[w]):
                                cost_so_far[w]=newcost
                                frontier.enqueue(w,newcost+maze.heuristic(w,goal))
                                came_from[w]=v
        return None
    def heuristic(self, a, b):
        x=abs(a[0]-b[0])
        y=abs(a[1]-b[1])
        return math.sqrt(x*x+y*y)
def drawPath(win, maze, came_from):
    offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    add = lambda x,y:x+y
    current = maze.goal
    while current != maze.start:
        next = came_from[current]
        for offset in offsets:
            next_one = tuple(map(add, current, offset))
            if next_one == next:
                line = Line(Point(next[1]+1+0.5, \
                                  maze.numRows()-next[0]+1-0.5), \
                            Point(current[1]+1+0.5, \
                                  maze.numRows()-current[0]+1-0.5))
                line.setOutline('white')
                line.setArrow('last')
                line.draw(win)
        current = next
def main():
    win = GraphWin('MazeDraw', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    mazedraw = MazeDraw(win, maze)
    mazedraw.draw()
    came_from = {}
    found = Maze.AStar(maze, maze.start, maze.came_from)
    text = Text(Point(11, 0.5), '')
    if found == maze.goal:
        text.setText('Goal found!')
        drawPath(win, maze, came_from)
    else:
        text.setText('Goal not found!')
    text.draw(win)


    while win.checkKey() != 'Escape':
        mazedraw.draw()
    win.close()

if __name__ == '__main__':
    main()

