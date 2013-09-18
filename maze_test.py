
from games.simple_maze import SimpleMaze
from lib.match import LocalMatch

from agents.random_agent import RandomAgent

print LocalMatch(SimpleMaze, [ RandomAgent ], rows=20, cols=20).play(print_state=True, delay=0.01)
