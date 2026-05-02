"""
# Block games.
/src/block_games_detroix23/life/interfaces.py
"""

from typing import TYPE_CHECKING

import pyxel

if TYPE_CHECKING:
	from block_games_detroix23.life import app
from block_games_detroix23 import vectors


class Ui:
	"""
	# Conway's game of life `Ui`.
	Draw mouse, grid, text.
	"""
	SPRITE_MOUSE_IMAGE: int = 0
	SPRITE_MOUSE_POSITION: vectors.Vector2D[int] = vectors.Vector2D(0, 0)
	SPRITE_MOUSE_SIZE: vectors.Vector2D[int] = vectors.Vector2D(16, 16)
	SPRITE_MOUSE_SCALE: float = 1.0
	SPRITE_MOUSE_ALPHA: int = 8

	parent_app: 'app.App'
	text_padding: vectors.Vector2D[int]

	def __init__(
		self, 
		parent_app: 'app.App',
		text_padding: vectors.Vector2D[int],	
	) -> None:
		"""
		Create the `Ui`.
		"""
		self.parent_app = parent_app
		self.text_padding = text_padding

	def draw(self) -> None:
		"""
		Draw using `pyxel` all text, cursor and grid.
		"""
		# Center.
		pyxel.rect(
			x=pyxel.width / 2,
			y=0.0,
			w=1.0,
			h=pyxel.height,
			col=pyxel.COLOR_GRAY,
		)
		pyxel.rect(
			x=0.0,
			y=pyxel.height / 2,
			w=pyxel.width,
			h=1,
			col=pyxel.COLOR_GRAY,
		)

		# Text.
		lines: list[str] = [
			f"Population: {len(self.parent_app.get_cells())}",
			f"Generation: {self.parent_app.plate.iteration}",
			f"Speed: {self.parent_app.time_speed}",
			f"Position: {self.parent_app.camera.position.x:.1f}; {self.parent_app.camera.position.y:.1f}",
			f"Zoom: {self.parent_app.camera.zoom:.3f}",
		]

		for y, line in enumerate(lines):
			pyxel.text(
				self.text_padding.x, 
				self.text_padding.y + 8 * y, 
				line, 
				pyxel.COLOR_WHITE,
			)
		
		# Cursor.
		pyxel.rect(
			x=pyxel.mouse_x,
			y=0.0,
			w=1.0,
			h=pyxel.height,
			col=pyxel.COLOR_LIME
		)
		pyxel.rect(
			x=0.0,
			y=pyxel.mouse_y,
			w=pyxel.width,
			h=1.0,
			col=pyxel.COLOR_LIME
		)

		pyxel.blt(
			pyxel.mouse_x - Ui.SPRITE_MOUSE_SIZE.x // 2,
			pyxel.mouse_y - Ui.SPRITE_MOUSE_SIZE.y // 2,
			img=Ui.SPRITE_MOUSE_IMAGE,
			u=Ui.SPRITE_MOUSE_POSITION.x,
			v=Ui.SPRITE_MOUSE_POSITION.y,
			w=Ui.SPRITE_MOUSE_SIZE.x,
			h=Ui.SPRITE_MOUSE_SIZE.y,
			scale=Ui.SPRITE_MOUSE_SCALE,
			colkey=Ui.SPRITE_MOUSE_ALPHA,
		)
