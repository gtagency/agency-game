#
# Copyright (C) 2013 Nick Johnson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of this Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTIBILITIY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OF OTHER DEALINGS IN
# THE SOFTWARE.
#

import random

class SimpleMaze(object):

    def __init__(self, player_count, cols=20, rows=20):
        if player_count != 1:
            raise TypeError, 'GridMaze requires 1 player (%d given)' % player_count
        
        self._cols = cols
        self._rows = rows
        self._maze = [ [ False for i in range(cols + 2) ]
                       for j in range(rows + 2) ]

        # generate maze using randomized Prim's Algorithm
        self._maze[1][1] = True
        frontier = [ (1, 2), (2, 1) ]
        while len(frontier) > 0:
            wall = frontier.pop(random.randint(0, len(frontier)-1))
            if sum(self._maze[wall[0] + delta[0]][wall[1] + delta[1]] 
                   for delta in [(0,1),(1,0),(0,-1),(-1,0)]) == 1:
                self._maze[wall[0]][wall[1]] = True
                frontier.extend([(wall[0] + delta[0], wall[1] + delta[1])
                                 for delta in [(0,1),(1,0),(0,-1),(-1,0)]
                                 if wall[0] + delta[0] > 0 and
                                    wall[1] + delta[1] > 0 and
                                    wall[0] + delta[0] <= rows and
                                    wall[1] + delta[1] <= cols])

        # guarantee that goal is accessible
        for i in range(min(cols, rows)):
            if self._maze[rows - i][cols - i] == False:
                self._maze[rows - i][cols - i] = True
            else:
                break

        # remove a few random walls to make the maze not a tree
        for i in range((cols + rows) / 4):
            for j in range(1000):
                wall = (random.randint(1, rows), random.randint(1, cols))
                if not self._maze[wall[0]][wall[1]]:
                    self._maze[wall[0]][wall[1]] = True
                    break

        self._move_count = 0
        self._position = [1, 1]
        self.results = None

    @property
    def player_config(self):
        return [
            {
                'maze' : self._maze,
                'cols' : self._cols,
                'rows' : self._rows
            }
        ]

    @property
    def state(self):
        return [
            {
                'maze' : self._maze,
                'cols' : self._cols,
                'rows' : self._rows,
                'position' : self._position
            }
        ]

    @property
    def valid_moves(self):
        moves = []
        for delta in [(0,1),(1,0),(0,-1),(-1,0)]:
            newpos = (self._position[0] + delta[0], self._position[1] + delta[1])
            if self._maze[newpos[0]][newpos[1]] == True:
                moves.append([delta[0], delta[1]])
        return [ moves ]

    def apply_moves(self, moves):
        move = moves[0]
        self._position[0] += move[0]
        self._position[1] += move[1]
        self._move_count += 1
        if self._position == [ self._rows, self._cols ]:
            self.results = [ self._move_count ]

    def __str__(self):
        output = []
        for i in range(len(self._maze)):
            output.append('\n')
            for j in range(len(self._maze[i])):
                if [i, j] == self._position:
                    output.append('*')
                elif self._maze[i][j]:
                    output.append(' ')
                else:
                    output.append('O')
        return ''.join(output)
