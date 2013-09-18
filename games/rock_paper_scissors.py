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

class RockPaperScissors(object):

    def __init__(self, player_count):
        if player_count != 2:
            raise TypeError, 'RockPaperScissors requires 2 players (%d given)' % player_count

    @property
    def player_config(self):
        return [ None, None ]

    @property
    def state(self):
        return [ None, None ]

    @property
    def valid_moves(self):
        return [
            [ 'rock', 'paper', 'scissors' ],
            [ 'rock', 'paper', 'scissors' ]
        ]

    def apply_moves(self, moves):
        r1 = ['rock', 'paper', 'scissors'].index(moves[0])
        r2 = ['rock', 'paper', 'scissors'].index(moves[1])
        self.results = [
            [[0.5, 0.5], [0.0, 1.0], [1.0, 0.0]],
            [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]],
            [[0.0, 0.1], [1.0, 0.0], [0.5, 0.5]]
        ][r1][r2]
