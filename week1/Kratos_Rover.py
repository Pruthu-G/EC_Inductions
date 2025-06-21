from collections import deque

class Position:
    """
    This is basically a point on the map

    Attributes:
        x: Row index
        y: Column index
        trav: 1 = traversable, 0 = blocked
    """
    def __init__(self, x, y, trav=1):
        self.x = x
        self.y = y
        self.trav = trav


class Map:
    """
    A grid made of points 

    Attributes:
        rows: Number of rows
        cols: Number of columns
        grid: 2D list of Position objects.
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Position(i, j, 1))
            self.grid.append(row)

    def block(self, x, y):
        """
        Makes a position non traversable.
        """
        if 0 <= x < self.rows and 0 <= y < self.cols:
            self.grid[x][y].trav = 0

class Rover:
    """
    A rover that moves on the map

    Attributes:
        battery: Battery percentage
        position: Current location
    """
    def __init__(self, position):
        self.position = position
        self.battery = 100

    def move_to(self, endx, endy, mapObj):
        """
        Move to (endx, endy) using DFS (any valid path).
        Uses 1% battery per step.

        Returns:
            steps taken (int), or -1 if unreachable
        """
        visited = [[False for _ in range(mapObj.cols)] for _ in range(mapObj.rows)]

        def dfs(x, y, steps):
            if x == endx and y == endy:
                return steps
            visited[x][y] = True

            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < mapObj.rows and 0 <= ny < mapObj.cols:
                    if not visited[nx][ny] and mapObj.grid[nx][ny].trav == 1:
                        result = dfs(nx, ny, steps + 1)
                        if result != -1:
                            return result  # stop at first valid path

            return -1  # dead end

        steps_taken = dfs(self.position.x, self.position.y, 0)

        if steps_taken != -1 and steps_taken <= self.battery:
            self.battery -= steps_taken
            self.position = mapObj.grid[endx][endy]
            return steps_taken

        return -1  # can't reach or not enough battery
