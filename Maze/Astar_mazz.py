from time import *
from random import *
from myqueue import Queue
from stack import Stack
from maze import *
from mazedraw import *
from graphics import *


def Astar(maze, came_from):
    frontier = Queue()
    cost_so_far = {}
    frontier.enqueue(maze,0)
    cost_so_far[maze.ToString()] = maze.cost
    came_from[maze.ToString()] = None
    while not frontier.is_empty():
        maze = frontier.dequeue()

        if maze.isGoal():
            return maze
        else:
            moves = maze.getAllMoves()
            for move in moves:
                newmaze = maze.clone()
                newmaze.move(*move)
                new_cost = newmaze.cost
                if cost_so_far.get(newmaze.ToString()) == None or \
                        new_cost < cost_so_far[newmaze.ToString()]:
                    cost_so_far[newmaze.ToString()] = new_cost
                    priority = new_cost + newmaze.heuristics
                    frontier.enqueue(newmaze, priority)
                    came_from[newmaze.ToString()] = newmaze
    return None
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
    win = GraphWin('DFS for Maze', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    mazedraw = MazeDraw(win, maze)
    mazedraw.draw()
    # visited = Array2D(maze.numRows(), maze.numCols())
    # visited.clear(False)
    came_from = {}
    found = Astar(maze,came_from)
    text = Text(Point(11, 0.5), '')
    if found == maze.goal:
        text.setText('Goal found!')
        drawPath(win, maze, came_from)
    else:
        text.setText('Goal not found!')
    text.draw(win)

    while win.checkKey() != 'Escape':
        pass
    win.close()

if __name__ == '__main__':
    main()
