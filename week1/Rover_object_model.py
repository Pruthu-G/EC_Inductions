class Position:
    """Represents a position in 2D space."""

    def __init__(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.traversable = traversable

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Map:
    """Represents the 2D map using a grid of Position objects."""

    def __init__(self, width, height):
        self.grid = [[Position(x, y) for y in range(height)] for x in range(width)]
        self.width = width
        self.height = height

    def set_block(self, x, y, traversable):
        """Mark a position as traversable or not."""
        self.grid[x][y].traversable = traversable

    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[x][y].traversable


class Rover:
    """Represents the Rover and its behavior."""

    def __init__(self, start_x, start_y, map_obj):
        self.battery = 100
        self.position = map_obj.grid[start_x][start_y]
        self.map = map_obj

    def move_to(self, dest_x, dest_y):
        """Moves rover to a destination using BFS and returns steps or -1 if not reachable."""
        from collections import deque

        if not self.map.is_valid(dest_x, dest_y):
            return -1

        visited = [[False] * self.map.height for _ in range(self.map.width)]
        queue = deque([(self.position.x, self.position.y, 0)])

        visited[self.position.x][self.position.y] = True
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            x, y, steps = queue.popleft()

            if x == dest_x and y == dest_y:
                required_battery = steps
                if required_battery > self.battery:
                    return -1
                self.battery -= required_battery
                self.position = self.map.grid[x][y]
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.map.is_valid(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1
