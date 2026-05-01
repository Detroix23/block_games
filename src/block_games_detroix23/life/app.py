# type: ignore
"""
# Block games.
/src/block_games_detroix23/life/app.py
"""

import pyxel

from block_games_detroix23 import vectors

class App:
	"""
	# Conway's game of life `App`.
	"""
	screen_size: vectors.Vector2D[int]

	def __init__(self, screen_size: vectors.Vector2D[int]) -> None:
		"""
		Initialize the `App` and the `pyxel` backend. Start the game with `run`.
		"""
		self.screen_size = screen_size

		print("(?) life.App.__init__() Initializing `pyxel`.")
		pyxel.init(
			screen_size.x, 
			screen_size.y,
			title="Conway's game of life.",
			fps=30,
			quit_key=pyxel.KEY_ESCAPE,
		)

	def run(self) -> None:
		"""
		Start the Conway's game.
		"""
		print("(?) life.App.run() Running `pyxel`.")
		pyxel.run(self.update, self.draw)


	def update(self) -> None:
		"""
		Update the state of the `App`.
		"""

	def draw(self) -> None:
		"""
		Draw the graphics.
		"""
