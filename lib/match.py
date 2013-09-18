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

import time
import sys

class LocalMatch(object):

    def __init__(self, game_class, agent_classes, **config):
        self._game_class = game_class
        self._agent_classes = agent_classes
        self._config = config

        self.game = None
        self.agents = None
        self.results = None

    def start(self):
        self.game = self._game_class(len(self._agent_classes), **self._config)
        agent_configs = self.game.player_config
        self.agents = [ self._agent_classes[i](**agent_configs[i])
                        for i in range(len(self._agent_classes)) ]

    def step(self):
        if self.results is not None:
            return
        state = self.game.state
        valid_moves = self.game.valid_moves
        moves = [ self.agents[i].select_move(state[i], valid_moves[i])
                  if valid_moves[i] is not None else None
                  for i in range(len(self.agents)) ]
        for i in range(len(moves)):
            if moves[i] is not None and moves[i] not in valid_moves[i]:
                raise ValueError, 'agent %d attempted invalid move %s' % (i, str(moves[i]))
        self.game.apply_moves(moves)
        self.results = self.game.results

    def play(self, print_state=False, delay=False):
        self.start()
        while self.results is None:
            self.step()
            if print_state:
                sys.stdout.flush()
                print self.game
                sys.stdout.flush()
            if delay:
                time.sleep(delay)
        return self.results
