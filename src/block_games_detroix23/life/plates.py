"""
# Block games.
/src/block_games_detroix23/life/plates.py
"""

from block_games_detroix23 import vectors

NEIGHBORS: list[vectors.Vector2D[int]] = [
	vectors.Vector2D(0, 1),
	vectors.Vector2D(1, 1),
	vectors.Vector2D(1, 0),
	vectors.Vector2D(1, -1),
	vectors.Vector2D(0, -1),
	vectors.Vector2D(-1, -1),
	vectors.Vector2D(-1, 0),
	vectors.Vector2D(-1, 1),
]

class Plate:
	"""
	# Conway's game of life `Plate` for the cells.
	Holds the cell position reference `set`, rules, `update` methods. 
	"""
	iteration: int
	cells: set[vectors.Vector2D[int]]
	underpopulation_threshold: int
	""" Die if neighbor count is strictly inferior. """
	overpopulation_threshold: int
	""" Die if neighbor count is strictly superior. """
	reproduction: int
	""" Spawn if neighbor count is equal. """

	def __init__(
		self, 
		starting_cells: set[vectors.Vector2D[int]],
		underpopulation_threshold: int,
		overpopulation_threshold: int,
		reproduction: int,
	) -> None:
		"""
		Initialize the `Plate`: `cells`, and rules. 
		"""
		self.iteration = 0
		self.cells = starting_cells
		self.underpopulation_threshold = underpopulation_threshold
		self.overpopulation_threshold = overpopulation_threshold
		self.reproduction = reproduction

	def count_neighbors(self, position: vectors.Vector2D[int]) -> int:
		"""
		Returns neighbor count.
		"""
		count: int = 0
		for relative in NEIGHBORS:
			if position + relative in self.cells:
				count += 1

		return count
	
	def is_alive(self, position: vectors.Vector2D[int]) -> bool:
		"""
		Check, according to the rules, if tile at `position` should be occupied by a living cell.
		"""
		neighbors: int = self.count_neighbors(position)
		live: bool = (
			position in self.cells and (
				neighbors >= self.underpopulation_threshold 
				and neighbors <= self.overpopulation_threshold
			)
			or neighbors == self.reproduction 
		)
		
		#print(f"(?) life.plates.Plate.is_alive({position}) n={neighbors}, in:{position in self.cells}, +:{live}")
		return live

	def update(self) -> None:
		"""
		General update of all cell in `cells`:
		- check its life;
		- look for reproduction in neighbor empty cells.
		"""
		new: set[vectors.Vector2D[int]] = set()

		for cell in self.cells:
			if self.is_alive(cell):
				new.add(cell)

			for relative in NEIGHBORS:
				neighbor: vectors.Vector2D[int] = cell + relative
				if (
					neighbor not in self.cells 
					and neighbor not in new
					and self.is_alive(neighbor)
				):
					new.add(neighbor)
		
		length_difference = len(self.cells) - len(new)
		changes = len(self.cells.symmetric_difference(new))
		print(f"(?) life.plates.Plate.update() d(length)={length_difference}, q(changes)={changes}")
		self.cells = new
