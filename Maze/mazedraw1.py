# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:02:19 2018

@author: duxiaoqin
Functions:
    (1)MazeDraw class
"""

from graphics import *
from maze import *

class MazeDraw:
    SUCCEED=1
    FAILED=0

    def __init__(self, win, maze):
        self.maze=maze;
        self.width = maze.numCols()
        self.height = maze.numRows()
        self.win = win
        self.win.setCoords(0.0, 0.0, self.width + 2, self.height + 2)
        self.rect_points = []
        for row in range(self.height):
            for col in range(self.width):
                point1 = Point(col+1, self.height-row)
                point2 = Point(col+1+1, self.height-row+1)
                if maze[row, col] == maze.EMPTY:
                    color = 'green'
                else:
                    color = 'blue'
                self.rect_points.append((point1, point2, color))
        self.rectangles = []
        for p1, p2, color in self.rect_points:
            rect = Rectangle(p1, p2)
            rect.setFill(color)
            self.rectangles.append(rect)
        
    def draw(self):
        for rect in self.rectangles:
            rect.undraw()
        for rect in self.rectangles:
            rect.draw(self.win)

        
        
    def DefSearch(self,row,col):
          if (col==self.width-1)and(row==self.height-1):
              point1 = Point(col+1, self.height-row)
              point2 = Point(col+1+1, self.height-row+1)
              color = 'black'
              rect = Rectangle(point1, point2)
              rect.setFill(color)
              rect.draw(self.win)
              return MazeDraw.SUCCEED
          else:
              if(row>=self.height)or(col>=self.width)or(self.maze[row,col]!=Maze.EMPTY):
                  return MazeDraw.FAILED
              else:
                  result=self.DefSearch(row+1,col)
                  if(result==MazeDraw.SUCCEED):
                      point1 = Point(col+1, self.height-row)
                      point2 = Point(col+1+1, self.height-row+1)
                      color = 'black'
                      rect = Rectangle(point1, point2)
                      rect.setFill(color)
                      rect.draw(self.win)
                      return result
                  else:
                      result=self.DefSearch(row,col+1)
                      if(result==MazeDraw.SUCCEED):
                           point1 = Point(col+1, self.height-row)
                           point2 = Point(col+1+1, self.height-row+1)
                           color = 'black'
                           rect = Rectangle(point1, point2)
                           rect.setFill(color)
                           rect.draw(self.win)
                           
                           return result
                      else:
                          return result

def main():
    win = GraphWin('MazeDraw', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    maze.print()
    mazedraw = MazeDraw(win, maze)
    while win.checkKey() != 'Escape':
        mazedraw.draw()
        result=mazedraw.DefSearch(0,0)
        
    win.close()
    
if __name__ == '__main__':
    main()