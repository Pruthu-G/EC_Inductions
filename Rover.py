from collections import deque

class Position:
    """
    Represents a coordinate on the map.

    Attributes:
        x (int): The x-coordinate.
        y (int): The y-coordinate.
        traversable (bool): Whether the position is traversable.
    """

    def __init__(self, x, y, traversable=True):
        """
        Initialize a Position object.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            traversable (bool): Indicates if this position can be traversed.
        """
        self.x = x
        self.y = y
        self.traversable = traversable

    def __eq__(self, other):
        """
        Check if two positions are equal based on x and y coordinates.

        Args:
            other (Position): Another position to compare.

        Returns:
            bool: True if positions match.
        """
        return self.x == other.x and self.y == other.y


class Map:
    """
    Represents a 2D grid of Position objects.

    Attributes:
        width (int): Width of the map.
        height (int): Height of the map.
        grid (list): 2D list of Position objects.
    """

    def __init__(self, width, height, grid=None):
        """
        Initialize the Map.

        Args:
            width (int): Width of the map.
            height (int): Height of the map.
            grid (list, optional): Custom 2D list of Position objects.
        """
        self.width = width
        self.height = height
        self.grid = grid if grid else [[Position(x, y, True) for y in range(height)] for x in range(width)]

    def get_position(self, x, y):
        """
        Get the Position object at a given coordinate.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            Position: The Position object at the given coordinates.
        """
        return self.grid[x][y]

    def is_valid(self, x, y):
        """
        Check if a given position is within bounds and traversable.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            bool: True if position is valid and traversable.
        """
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[x][y].traversable


class Rover:
    """
    Represents a rover with battery and position that can traverse a map.

    Attributes:
        current_position (Position): The rover's current position.
        battery (int): Battery level as a percentage (0-100).
    """

    def __init__(self, start_pos):
        """
        Initialize the rover.

        Args:
            start_pos (Position): Starting position of the rover.
        """
        self.current_position = start_pos
        self.battery = 100

    def traverse(self, target_pos, map_obj):
        """
        Traverse the map from current position to the target position.

        Uses Breadth-First Search (BFS) to find the shortest path.

        Args:
            target_pos (Position): Destination position.
            map_obj (Map): The map to be traversed.

        Returns:
            int: Number of steps taken, or -1 if path is not possible or battery insufficient.
        """
        start = self.current_position
        goal = target_pos

        if not map_obj.is_valid(goal.x, goal.y):
            return -1

        visited = [[False] * map_obj.height for _ in range(map_obj.width)]
        queue = deque([(start.x, start.y, 0)])  # (x, y, steps)
        visited[start.x][start.y] = True

        while queue:
            x, y, steps = queue.popleft()

            if x == goal.x and y == goal.y:
                if steps > self.battery:
                    return -1
                self.battery -= steps
                self.current_position = Position(x, y)
                return steps

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if map_obj.is_valid(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1  # Path not found
