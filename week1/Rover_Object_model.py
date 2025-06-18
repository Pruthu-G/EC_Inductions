from collections import deque

class Position:
    """
    This class is used to store the x and y coordinate of a cell in the grid.
    It also checks if the rover can go through that cell or not.
    """
    def __init__(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.traversable = traversable

    def is_traversable(self):
        """
        This function tells if the rover can move through this position.
        """
        return self.traversable


class Map:
    """
    This class creates a 10x10 grid made up of Position objects.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.create_grid()

    def create_grid(self):
        """
        This function creates the 2D array of Position objects.
        """
        grid = []
        for row in range(10):
            row_list = []
            for col in range(10):
                pos = Position(col, row)
                row_list.append(pos)
            grid.append(row_list)
        return grid

    def get_position(self, x, y):
        """
        This function returns the Position at x, y if it's inside the grid.
        """
        if 0 <= x < 10 and 0 <= y < 10:
            return self.grid[y][x]
        else:
            return None

    def is_inside_map(self, x, y):
        """
        Check if the x and y are valid positions on the map.
        """
        return 0 <= x < 10 and 0 <= y < 10


class Rover:
    """
    This class represents the Rover with a battery and current location.
    """
    def __init__(self, start_position, battery=100.0):
        self.current_location = start_position
        self.battery = battery

    def traverse(self, dest_x, dest_y, map_obj):
        """
        This function helps the rover move from its current location
        to the destination (dest_x, dest_y). It returns number of steps,
        or -1 if it can't reach the destination.
        """
        start_x = self.current_location.x
        start_y = self.current_location.y

        start = (start_x, start_y)
        end = (dest_x, dest_y)

        destination_cell = map_obj.get_position(dest_x, dest_y)
        if destination_cell is None or not destination_cell.is_traversable():
            return -1

        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        # Only non-diagonal directions: left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            current, steps = queue.popleft()
            current_x, current_y = current

            if current == end:
                self.current_location = map_obj.get_position(current_x, current_y)
                self.battery = self.battery - (steps * 1)
                if self.battery < 0:
                    self.battery = 0
                return steps

            for dx, dy in directions:
                new_x = current_x + dx
                new_y = current_y + dy
                new_position = (new_x, new_y)

                if new_position not in visited:
                    if map_obj.is_inside_map(new_x, new_y):
                        next_cell = map_obj.get_position(new_x, new_y)
                        if next_cell is not None and next_cell.is_traversable():
                            queue.append((new_position, steps + 1))
                            visited.add(new_position)

        return -1  # If no path is found


