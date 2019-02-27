# knightstour

 Finds a "knight's tour" of an n x n chessboard. A knight's tour is a
 sequence of moves that a knight can take where the knight only visits
 each square once. Mind that a knight moves in an "L" shape across the 
 board. from any point. Here's some glorious ascii art demonstrating the
 possible moves a knight has from a particular point. At most, the knight
 can have 8 possible destinations. In practice, there will probably be
 fewer possibilities.
 
 ```
 [ ][*][ ][*][ ]
 [*][ ][ ][ ][*]
 [ ][ ][N][ ][ ]
 [*][ ][ ][ ][*]
 [ ][*][ ][*][ ]
 ```
 so, the night must move 2 spaces along the x axis then one space along the y
 axis. the direction is determined by the size of the graph.
 
 One way of optimizing the traversal of the knight is employing warnsdorf's
 rule, a heuristic that chooses which space the knight should move to given
 a number of options. in this heuristic, the knight will always choose to move  to 
 a space based on the fewest amount of possible moves.
 
 this graph is a non-directed graph, but the knight cannot visit any spaces 
 which it has already visited.
 
 once the code for traversing the graph is completed, i hope to implement
 a graphical representation of the tour using Zelle's graphics.py module. 
 
 nick creel - algorithms - spring 2019 - marlboro college
 GNU GPL https://www.gnu.org/licenses/gpl.html
