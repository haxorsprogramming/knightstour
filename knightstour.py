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
from operator import add

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
    result = tuple(map(add, atuple, btuple))    
    return result

def generateBoard(board, n):
    '''
    constructs a dictionary of nodes, where each node is a key
    that points to an empty list. this list will contain the
    neighbors of that particular node.
    '''
    for x in range(n):
        for y in range(n):
            board.nodes[(x,y)].append(())

def findMoves(board):
    '''
    for each node in board.nodes, findNeighbor creates a list of possible
    neighbors. if those possible neighbors exist in board.nodes, then
    findNeighbor appends the list that node points to, including the 
    confirmed neighbor. if neighbor is not in board.nodes, nothing happens. 
    '''
    for key in board.nodes:
        for move in knightmoves:
            # debug print(key)
            # debug print(knightmoves[move])
            temp = tuple(map(sum, zip(key, knightmoves[move])))
            if temp in board.nodes:
                board.nodes[key].append(temp) 
            else:
                pass

def main():
    chessboard = Graph()
    generateBoard(chessboard, 5)
    print("Board nodes: " + str(chessboard.nodes.keys()))
    #debug  print("Possible moves (empty): " + str(chessboard.nodes.values()))
    findMoves(chessboard)
    print("Possible moves (shouldn't be empty: " +str(chessboard.nodes.values()))

main() 
        
