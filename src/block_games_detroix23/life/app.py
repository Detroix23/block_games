"""
# Block games.
/src/block_games_detroix23/life/app.py
"""

import pyxel

from block_games_detroix23 import definitions, vectors
from block_games_detroix23.life import plates, cameras, interfaces

class App:
	"""
	# Conway's game of life `App`.
	"""

	plate: plates.Plate
	camera: cameras.Camera
	ui: interfaces.Ui
	screen_size: vectors.Vector2D[int]
	time_speed: int
	""" Frame between updates. """

	def __init__(self, screen_size: vectors.Vector2D[int]) -> None:
		"""
		Initialize the `App` and the `pyxel` backend. Start the game with `run`.
		"""
		self.screen_size = screen_size
		self.plate = plates.Plate(
			starting_cells={
				vectors.Vector2D(0, 1),
				vectors.Vector2D(0, 0),
				vectors.Vector2D(0, -1),
			},
			underpopulation_threshold=2,
			overpopulation_threshold=3,
			reproduction=3,
		)
		self.camera = cameras.Camera(
			parent_app=self,
			zoom=1.0,
			position=vectors.Vector2D(0.0, 0.0),
			move_speed=3.0,
			scroll_speed=1.5,
			disable_sprite=False,
		)
		self.ui = interfaces.Ui(
			parent_app=self,
			text_padding=vectors.Vector2D(2, 2),
		)
		self.time_speed = 1

		print("(?) life.App.__init__() Initializing `pyxel`.")
		pyxel.init(
			screen_size.x, 
			screen_size.y,
			title="Conway's game of life.",
			fps=25,
			quit_key=pyxel.KEY_ESCAPE,
		)

		pyxel.load(str(definitions.PATH_RESSOURCE_LIFE))

	def get_cells(self) -> set[vectors.Vector2D[int]]:
		"""
		Returns `plate`'s `cells`.
		"""
		return self.plate.cells

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
		self.plate.update()
		self.camera.update()

	def draw(self) -> None:
		"""
		Draw the graphics.
		"""
		pyxel.cls(pyxel.COLOR_BLACK)
		self.camera.draw()
		self.ui.draw()
