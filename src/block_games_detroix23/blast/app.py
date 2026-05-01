"""
# Block games.
/src/block_games_detroix23/blast/app.py
"""

import numpy
import pyxel

from block_games_detroix23 import vectors

class App:
	"""
	# Block blast `App`.
	"""
	screen_size: vectors.Vector2D[int]
	grid_size: vectors.Vector2D[int]
	grid: numpy.ndarray[tuple[int, int], numpy.dtype[numpy.uint8]]

	def __init__(
		self, 
		screen_size: vectors.Vector2D[int],
		grid_size: vectors.Vector2D[int],
	) -> None:
		self.screen_size = screen_size
		self.grid_size = grid_size
		self.grid = numpy.zeros(self.grid_size.tuple(), dtype=numpy.uint8)
		
		print("(?) blast.app.App() Pyxel initializing...")
		pyxel.init(
			width=self.screen_size.x, 
			height=self.screen_size.y,
			title="Block blast.",
			fps=30,
			quit_key=pyxel.KEY_ESCAPE, 
		)

	def start(self) -> None:
		"""
		Starts the application and `pyxel` envent loop.
		"""
		print("(?) blast.app.App() Run starting...")
		pyxel.run(self.update, self.draw)

	def update(self) -> None:
		"""
		`App` frame: update states. 
		"""
		

	def draw(self) -> None:
		"""
		`App` frame: draw to the screen.
		"""