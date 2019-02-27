'''
knightstour.py

Finds a "knight's tour" of an n x n chessboard. A knight's tour is a
sequence of moves that a knight can take where the knight only visits
each square once. Mind that a knight moves in an "L" shape across the 
board. from any point. Here's some glorious ascii art demonstrating the
possible moves a knight has from a particular point. At most, the knight
can have 8 possible destinations. In practice, there will probably be
fewer possibilities.

[ ][*][ ][*][ ]
[*][ ][ ][ ][*]
[ ][ ][N][ ][ ]
[*][ ][ ][ ][*]
[ ][*][ ][*][ ]

so, the night must move 2 spaces along the x axis then one space along the y
axis. the direction is determined by the size of the graph.

One way of optimizing the traversal of the knight is employing warnsdorf's
rule, a heuristic that chooses which space the knight should move to given
a number of options. in this heuristic, the knight will always choose to move to 
a space based on the fewest amount of possible moves.

this graph is a non-directed graph, but the knight cannot visit any spaces 
which it has already visited.

once the code for traversing the graph is completed, i hope to implement
a graphical representation of the tour using Zelle's graphics.py module. 

nick creel - algorithms - spring 2019 - marlboro college
GNU GPL https://www.gnu.org/licenses/gpl.html
'''
from collections import defaultdict
from turtle import *
import re

knightmoves = { 'upleft' : (-1,2),  #all the possible moves the knight can make
        'upright' : (1,2),  #defined as a tuple of x,y transformations 
        'leftdown' : (-2,-1),   #(these numbers are added or subtracted
        'leftup' : (-2, 1),    #from actual current location to move)
        'rightdown' : (2,-1),
        'rightup' : (2,1),
        'downleft' : (-1,-2),
        'downright' : (1,-2),
        }

class Stack():  #last in first out, works for DFS
    def __init__(self):
        self.values = []
    def push(self, value):
        self.values.append(value)
    def pop(self):
        self.values.pop()
    def __len__(self):
        return len(self.values)

class Graph():
    def __init__(self, direction = False):
        self.nodes = defaultdict(list)
        self.direction = direction

def addTuple(atuple, btuple):
    '''
    a lovely solution for adding the elements of a tuple
    that I discovered on stack exchange after a lot of
    whining about how python adds tuples by default.

    https://stackoverflow.com/questions/497885/python-element-wise-tuple-operations-like-sum

    thanks ironfroggy!

    >>> atuple = (1,2,3)
    >>> btuple = (4,5,6)
    >>> addTuple(atuple, btuple)
    (5,7,9)
    '''
    result = tuple(map(sum, zip(atuple, btuple)))    
    return result

def findMoves(board):
    '''
    for each node in board.nodes, findNeighbor creates a list of possible
    neighbors. if those possible neighbors exist in board.nodes, then
    findNeighbor appends the list that node points to, including the 
    confirmed neighbor. if neighbor is not in board.nodes, nothing happens.i


    '''
    for key in board.nodes:
        for move in knightmoves:
            # debug print(key)
            # debug print(knightmoves[move])
            temp = addTuple(key, knightmoves[move])
            if temp in board.nodes:
                board.nodes[key].append(temp) 
            else:
                pass

def generateBoard(board, n):
    '''
    constructs a dictionary of nodes, where each node is a key
    that points to an empty list. this list will contain the
    neighbors of that particular node.
    '''
    for x in range(n):
        for y in range(n):
            board.nodes[(x,y)] = []

def knightTour(board, start, movespossible, stack):
    temp = {}
    #print("debug start: {}".format(start)) 
    for value in board.nodes[start]:
        if value in stack.values and value in board.nodes:
            del board.nodes[value]
            pass
        elif value in stack.values and value not in board.nodes:
            pass
        else:
            temp[value] = movespossible[value]
    try:
        minimum = min(temp, key = temp.get)
    except ValueError:
        return stack.values
    stack.push(minimum)
    #print("debug possible destinations: {}".format(board.nodes[start]))
    #print("debug stack: {}".format(stack.values))
    #print("debug mimimum: {}".format(minimum))
    #print("debug temp: {}".format(temp))
    knightTour(board, minimum, movespossible, stack)

def numMoves(board):
    '''
    iterates over all possible moves to determine how many moves are
    from each node...I know this can be done with a general len test
    but I didn't want to have a dictionary of dictionaries storing the 
    visited flag or remove vertices from the graph if they were already
    visited. movesPossible will be used to determin the next node to visit
    via Warnsdorf's rule
    '''
    movespossible = {}
    for i in board.nodes:
        length = len(board.nodes[i])
        movespossible[i] = length
    return movespossible


def main():
    visited = Stack()
    chessboard = Graph()
    n = input("hello! this program calculates a knight's tour starting at a particular point on an n x n chess board. What size would you like the chessboard to be? Please enter a natural number, I'm not built to deal with errors just yet :)\n >>> ")
    n = int(n)
    if n > 0 and type(n) == int:
        generateBoard(chessboard, n)
    else:
        print("You broke it! that wasn't what I asked for at all...try again")
    print("Board nodes: " + str(chessboard.nodes.keys()))
    #debug  print("Possible moves (empty): " + str(chessboard.nodes.values()))
    findMoves(chessboard)
    #debug print("Possible moves (shouldn't be empty: " +str(chessboard.nodes.values()))
    nmoves = numMoves(chessboard)
    start = input("please enter a possible node from the list above like so: 0,0\n >>>")
    start = start.split(',')
    start = [int(start[n]) for n in range(len(start))]
    start = tuple(start)  
    visited.push(start)
    knightTour(chessboard, start, nmoves, visited)
    print("Visited nodes in Knight's Tour: " + str(visited.values))
    
    
    t = Turtle(shape = "circle") #time to draw a graph
    t.pencolor("blue")
    screen = t.getscreen()
    screen.setworldcoordinates(0,0,n,n)
    xturtle = Turtle(shape = "turtle")
    yturtle = Turtle(shape = "turtle")
    xturtle.speed(100)
    yturtle.speed(100)
    t.speed(5)
    for row in range(0,n):
        for column in range(0,n):
            xturtle.goto(row, column)
            xturtle.goto(row+1, column)
            xturtle.goto(row+1, column+1)
            yturtle.goto(row,column)
            yturtle.goto(row, column+1)
            yturtle.goto(row+1, column+1)
    t.goto(0.5, 0.5)
    for value in visited.values:
        t.goto(value[0]+0.5, value[1]+0.5)
    screen.exitonclick()
main() 
        
