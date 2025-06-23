

class Position:
    """
    Position specifies the x and y coordinates of a certain position,
and should also hold information about whether the particular coordinate is
traversable or not.

    Attributes:
        x: Row index
        y: Column index
        traversable: 1 = traversable, 0 = not traversable
     """
    def __init__(self, x, y, traversable=1):
        self.x = x
        self.y = y
        self.traversable = traversable
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Map:
    """
    Map acts as a grid of position object by using 2d arrays.

    Attributes:
        width: columns
        height: rows
        grid: 2D list of positions
    """    
     def __init__(self, width, height, traversable_matrix=0):
        self.width = width
        self.height = height
        self.grid = [
            [Position(x, y, traversable_matrix[y][x] if traversable_matrix else True)
             for x in range(width)]
            for y in range(height)
        ]

    def get_position(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

class Rover:
    """
    Represents a rover on the map.

    Attributes:
        battery (int): Remaining battery percentage.
        current_position (Position): The current position of the rover.
    """
    def __init__(self, start_position):
        self.battery = 100
        self.current_position = start_position
    
    def traverse(self, target_x, target_y, map_obj):
        """
        Args:
            target_x (int): Target row
            target_y (int): Target column
            map_obj (Map): Map object

        Returns:
            int: Steps taken, or -1 if target unreachable or battery insufficient.
        """
        target_position = map_obj.get_position(target_x, target_y)
        if not target_position or not target_position.traversable:
            return -1

        start = self.current_position
        visited = set()
        queue = deque([(start, 0)])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    