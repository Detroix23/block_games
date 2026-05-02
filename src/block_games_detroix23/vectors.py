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

	def __hash__(self) -> int:
		"""
		Compute an unique hash code.

		For `int`, uses:
		```
		(x + y) * (x + y + 1) / 2 + y
		```
		[Source](https://stackoverflow.com/questions/28618441/a-bijective-function-from-nnn-to-n)

		For `float`, uses:
		```python
		hash(self.tuple())
		```
		"""
		if isinstance(self.x, int) and isinstance(self.y, int):
			code: int = (self.x + self.y) * (self.x + self.y + 1) // 2 + self.y
			# print(f"(?) Vector.__hash__() code={code}")
			return code
		else:
			return hash(self.tuple())

	def __eq__(self, other: object) -> bool:
		if isinstance(other, Vector2D):
			return self.x == other.x and self.y == other.y  # type: ignore
		else:
			return False

	def __add__(self: Vector2D[int], other: Vector2D[int]) -> Vector2D[int]:
		"""
		Return a _new_ `Vector2D` by adding.
		"""
		return Vector2D(
			self.x + other.x,
			self.y + other.y
		)

	def __str__(self) -> str:
		return f"({self.x}; {self.y})"
	
	def __repr__(self) -> str:
		return f"Vector2D[{T_VEC.__class__.__name__}](x={self.x}, y={self.y})"

	def tuple(self) -> tuple[T_VEC, T_VEC]:
		"""
		Returns a `tuple[T_VEC, T_VEC]` representation of `self`.
		"""
		return (self.x, self.y)
	