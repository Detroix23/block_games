"""
# Block games.
/src/block_games_detroix23/life/cameras.py
"""

import math
from typing import TYPE_CHECKING

import pyxel

if TYPE_CHECKING:
	from block_games_detroix23.life import app
from block_games_detroix23 import vectors

class Camera:
	"""
	# Conway's game of life `Camera`.
	Move point-of-view, update zoom, and draw accordingly the cells.
	"""
	SPRITE_CELL_IMAGE: int = 0
	SPRITE_CELL_POSITION: vectors.Vector2D[int] = vectors.Vector2D(0, 16)
	SPRITE_CELL_SIZE: vectors.Vector2D[int] = vectors.Vector2D(16, 16)
	SPRITE_CELL_SCALE: float = 1.0 / 16.0


	parent_app: 'app.App'
	zoom: float
	position: vectors.Vector2D[float]
	move_speed: float
	scroll_speed: float

	def __init__(
		self, 
		parent_app: 'app.App',
		zoom: float, 
		position: vectors.Vector2D[float],
		move_speed: float,
		scroll_speed: float,
	) -> None:
		self.parent_app = parent_app
		self.zoom = zoom
		self.position = position
		self.move_speed = move_speed
		self.scroll_speed = scroll_speed

	def get_displacement_speed(self) -> float:
		"""
		Return the `move_speed` altered by `zoom`.
		"""
		return self.move_speed * math.sqrt(self.zoom)
 
	def update(self) -> None:
		"""
		Update the `Camera`. Listen to inputs.
		"""
		
		if pyxel.btn(pyxel.KEY_LEFT):
			self.position.x += self.get_displacement_speed()
		if pyxel.btn(pyxel.KEY_RIGHT):
			self.position.x -= self.get_displacement_speed()
		if pyxel.btn(pyxel.KEY_UP):
			self.position.y += self.get_displacement_speed()
		if pyxel.btn(pyxel.KEY_DOWN):
			self.position.y -= self.get_displacement_speed()

		if pyxel.mouse_wheel > 0:
			self.zoom *= self.scroll_speed * pyxel.mouse_wheel
			print(f"(?) life.cameras.Camera.update() zoom={self.zoom}")
		elif pyxel.mouse_wheel < 0 and self.zoom > 1.0:
			self.zoom /= self.scroll_speed * abs(pyxel.mouse_wheel)
			self.zoom = max(self.zoom, 1.0)
			print(f"(?) life.cameras.Camera.update() zoom={self.zoom}")

	def draw(self) -> None:
		"""
		Draw, to `pyxel` screen, all cells.
		"""
		if self.zoom > 1.0:
			for cell in self.parent_app.get_cells():
				x: float = cell.x * self.zoom - self.position.x - Camera.SPRITE_CELL_SIZE.x / 2
				y: float = cell.y * self.zoom - self.position.y - Camera.SPRITE_CELL_SIZE.y / 2
				pyxel.blt(
					x,
					y,
					img=Camera.SPRITE_CELL_IMAGE,
					u=Camera.SPRITE_CELL_POSITION.x,
					v=Camera.SPRITE_CELL_POSITION.y,
					w=Camera.SPRITE_CELL_SIZE.x,
					h=Camera.SPRITE_CELL_SIZE.y,
					scale=Camera.SPRITE_CELL_SCALE * self.zoom,
				)
		else:
			for cell in self.parent_app.get_cells():
				x: float = cell.x * self.zoom - self.position.x
				y: float = cell.y * self.zoom - self.position.y
				pyxel.rect(
					x,
					y,
					w=1.0,
					h=1.0,
					col=pyxel.COLOR_WHITE,
				)