# a-star-search.py
# ---------------------
# Attempts to find the most effecient path between two points using a* search

import sys

# Create empty grid with default size of 10x10
def create_empty_grid(m=10, n=10):
	grid = [[0] * m for i in range(n)]
	display(grid)
	return

def display(grid):
	for i in range(len(grid)):
		print(grid[i])

if __name__ == "__main__":
	if len(sys.argv) == 3:
		create_empty_grid(int(sys.argv[1]), int(sys.argv[2]))
	else:
		create_empty_grid()
