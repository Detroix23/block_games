"""
# Block games.
/src/block_games_detroix23/vectors.py
"""

from typing import Union, TypeVar, Generic

T_VEC = TypeVar("T_VEC", bound=Union[int, float])
""" `T_VEC`: `int` | `float`, generic type for `Vector2D`. """

class Vector2D(Generic[T_VEC]):
	x: T_VEC
	y: T_VEC

	def __init__(self, x: T_VEC, y: T_VEC) -> None:
		"""
		Initialize a `Vector2D` with 2 coordinates (`x`; `y`) of type `T_VEC`.

		**Types:**
		- `T_VEC` can be `int`, `float`. 
		"""
		super().__init__()
		self.x = x
		self.y = y

	def tuple(self) -> tuple[T_VEC, T_VEC]:
		"""
		Returns a `tuple[T_VEC, T_VEC]` representation of `self`.
		"""
		return (self.x, self.y)