class Position:
    """
    Represents a position on a grid with x y coordinates and traversability status
    """
    def __init__(self, x, y, traversable = True):
        """
        Initialize a Position instance
        Args: 
            x(int): x coordinate
            y(int): y coordinate
            traversable(bool): tells whether the position is traversable or not
        """
        self.x = x
        self.y = y
        self.traversable = traversable
class Map:
    """
    Represents a grid like map made of Position objects
    """
    def __init__(self, rows, cols):
        """
        Args:
            rows(int) : number of rows
            cols(int) : number of columns
        Attributes:
            grid (2d list) : 2d grid of position objects
        """
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Position(i, j))
            self.grid.append(row)
    def obstacle(self, x, y):
        """
        If there are any obstacles specified this function will mark that
        position as non traversable
        """
        self.grid[x][y].traversable = False
    def is_traversable(self, x, y):
        """
        Checks if the given position is traversable or not
        """
        if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y].traversable: 
            return True 
        else: 
            return False
        
class Rover:
    """
    Represents a rover class with battery life and current position
    Attributes:
        battery(int): current battery remaining
        current_pos (Position): current position of the rover
    """
    def __init__(self, start_pos):
        """
        Initializes a rover with full battery life and a starting position
        """
        self.battery = 100
        self.current_pos = start_pos
    def traverse(self, target_pos, m):
        """
        Moves the rover from its current position to a target position on the map

        Args: 
            target_pos(Position): the target position to move to
            m (Map): quite literally the map
        Returns:
            Number of steps taken or -1 if traversal is not possible
        """
        start = (self.current_pos.x, self.current_pos.y)
        target = (target_pos.x, target_pos.y)

        if not (m.is_traversable(start[0], start[1]) and m.is_traversable(target[0], target[1])):
            return -1

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        q = []
        q.append((start[0], start[1], 0))
        visited.add(start)

        while (q):
            x, y, steps = q.pop(0)
            if (x, y) == target:
                if steps <= self.battery:
                    self.current_pos = m.grid[x][y]
                    self.battery -= steps
                    return steps
                else:
                    return -1
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if m.is_traversable(nx, ny):
                    if (nx, ny) not in visited and m.grid[nx][ny].traversable:
                        visited.add((nx, ny))
                        q.append((nx, ny, steps+1))



if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    m = Map(rows, cols)

    rover = Rover(m.grid[0][0])
    steps = rover.traverse(m.grid[4][4], m)

    print("steps taken: ", steps)