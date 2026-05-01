"""
# Block games.
/src/block_games_detroix23/__main__.py
"""

from block_games_detroix23 import vectors, blast, life

def main() -> None:
	"""
	Block games: main entry point.
	"""

	run_life()
	

def run_blast() -> None:
	blast_app = blast.app.App(
		screen_size=vectors.Vector2D(500, 400),
		grid_size=vectors.Vector2D(8, 8),
	)
	
	blast_app.start()

def run_life() -> None:
	life_app = life.app.App(
		screen_size=vectors.Vector2D(500, 400),
	)

	life_app.run()

main()
