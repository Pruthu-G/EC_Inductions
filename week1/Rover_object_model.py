"""
Rover Object Model

This program models a rover navigating a 2D map using object-oriented programming .

Classes:
    Position: represents a coordinate and whether it's traversable.
    Map: a grid of Position objects.
    Rover: holds battery and current position, and can traverse the map.
"""

class Position:
    """
    Represents a coordinate (x, y) on the map.
    x (int): X-coordinate.
    y (int): Y-coordinate.
    traversable (bool): True if the cell can be visited, False otherwise.
    """
    def __init__(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.traversable = traversable


class Map:
    """
    Represents the map as a 2D grid of Position objects.

    Attributes:
        width (int): Number of columns.
        height (int): Number of rows.
        grid (list[list[Position]]): 2D array of positions.

    Methods:
        block(x, y): Marks a cell as non-traversable.
        is_valid(x, y): Checks bounds and traversability of a cell.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Position(x, y) for y in range(height)] for x in range(width)]

    def block(self, x, y):
        """Marks (x, y) as an obstacle (non-traversable)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y].traversable = False

    def is_valid(self, x, y):
        """Checks if (x, y) is within bounds and traversable."""
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[x][y].traversable


class Rover:
    """
    Represents a rover with a position and battery life.

    position (Position): Current position of the rover.
    battery (float): Battery percentage (starts at 100%).

    Methods:
        traverse(target_x, target_y, map_obj): 
            Moves the rover to the target if reachable within battery limits.
    """
    def __init__(self, position):
        self.position = position
        self.battery = 100.0

    def traverse(self, target_x, target_y, map_obj):
        """
        Tries to move the rover to the target position using BFS.
        Only moves non-diagonally and consumes 1% battery per step.

        target_x (int): Target x-coordinate.
        target_y (int): Target y-coordinate.
        map_obj (Map): The map the rover navigates.

        Returns:
            int: Steps taken if reachable and enough battery; otherwise -1.
        """
        visited = [[False for i in range(map_obj.height)] for j in range(map_obj.width)]
        queue = [(self.position.x, self.position.y, 0)]  # (x, y, steps)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while queue:
            x, y, steps = queue.pop(0)

            if steps > self.battery:
                return -1  # Not enough battery

            if x == target_x and y == target_y:
                self.position = map_obj.grid[x][y]
                self.battery -= steps
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if map_obj.is_valid(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1  # Target unreachable


