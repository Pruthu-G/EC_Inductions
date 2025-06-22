from collections import deque

class Position:
    """
    Represents a coordinate on the map.
    
    Attributes:
        x (int) : The x-coordinate.
        y (int) : The y-coordinate.
        traversible (bool) : Whether the rover can traverse this position.
    """
    def __init__(self, x, y):
        """
        Initialize a Position object.

        Args:
            x (int) : The x-coordinate.
            y (int) : The y-coordinate.
        """
        self.x = x
        self.y = y
        self.traversible = True

class Map:
    """
    Represents the map grid consisting of Position objects.

    Attributes:
        height (int) : Number of rows in the map.
        width (int): Number of columns in the map.
        grid (list of list of positions) : 2D list storing Position objects.
    """
    def __init__(self, height, width):
        """
        Initialize the Map with given dimensions, creating a grid of Positions.

        Args:
            height (int) : Number of rows.
            width (int): Number of columns.
        """
        self.height = height
        self.width = width
        self.grid = [
            [Position(x, y) for x in range(width)]
            for y in range(height)]

    def set_nontraversible(self, x, y):
        """
        Mark a specific position on the map as non-traversible (obstacle).

        Args:
            x (int): x-coordinate of the position.
            y (int): y-coordinate of the position.
        """
        self.grid[y][x].traversible = False

class Rover:
    """
    Represents a rover with battery life and current position.

    Attributes:
        batterylife (int) : Remaining battery life as a percentage (0-100).
        currentposition (Position): The rover's current location on the map.
    """
    def __init__(self, currentposition):
        """
        Initialize the Rover with a starting position and full battery.

        Args:
            currentposition (Position): Starting position of the rover.
        """
        self.batterylife = 100
        self.currentposition = currentposition

    def traverse(self, targetposition, mapp):
        """
        Traverse from the current position to a target position on the map.(uses Breadth-First Search (BFS))
        
        IMPLEMENTATION LOGIC:

        First creates a 2D list to keep track of visited positions to avoid revisiting.
        
        BFS starts from start position with steps=0,
        a queue is created with first element as start position and steps=0.
        
        Has an Outer loop (while loop) runs while queue is not empty,
        first element of queue is popped and checked for target position.
        If popped element is not target position, 
        An inner loop (for loop) is executed, it identifies cells adjacent to popped position that are traversible, 
        non visitted, within map and appends these positions along with steps+1 to the queue.

        Each time outer loop runs, an element is popped from front of queue.
        If the popped element is target position, we check steps to see if battery is sufficient or not and return steps accordingly.
        Else the inner loop is executed, which finds possible adjacent positions (traversible, not visitted, within the map) and 
        appends these along with steps+1 to the queue.

        If queue becomes empty, target can't be reached, outer loop exits, return -1

        
        Args:
            targetposition (Position): The destination position to reach.
            mapp (Map): The map to traverse on.

        Returns:
            int: Number of steps taken if traversal successful and battery sufficient.
                 Returns -1 if the target is unreachable or battery is insufficient.

        """
        height = mapp.height
        width = mapp.width

        # 2D list to track visited positions and avoid revisiting 
        visited = [[False for _ in range(width)] for _ in range(height)] 
        
        queue = deque()
        start_x, start_y = self.currentposition.x, self.currentposition.y
        
        # Start BFS from current rover position with 0 steps taken
        queue.append((start_x, start_y, 0))
        visited[start_y][start_x] = True

        # Possible moves: left, right, up, down (no diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    
        # Outer loop which runs until queue is not empty,
        # first element of queue is popped and checked for target position.
        # Has an inner loop which identifies cells adjacent to popped position which are traversible, 
        # non visitted, within map and appends these positions to the queue.
        
        while queue:
            x, y, steps = queue.popleft()

            # Check if target position reached
            if x == targetposition.x and y == targetposition.y:
                # Check if battery is sufficient for the steps
                if self.batterylife >= steps:
                    self.batterylife -= steps  # battery remaining
                    return steps

                else:
                    # Not enough battery to reach target
                    return -1

            # Inner loop, Explore adjacent positions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check bounds, traversibility, and if not visited yet
                if (0 <= nx < width and 0 <= ny < height and mapp.grid[ny][nx].traversible and not visited[ny][nx]):
                    visited[ny][nx] = True
                    queue.append((nx, ny, steps + 1))

        # Target not reachable
        return -1

def main():
    """
    main function i used to test my code.
    here are couple test cases i ran...

    ---------------------------------------------------------

    Test case 1 (target reachable):

    input:
    map height = 7
    map width = 9
    non traversible positions: (2,3);(3,3);(4,3);(5,3);
                               (4,4);(4,5);(4,6);
                               (6,2);(8,0);(0,0)
    start position = (1,3)
    target position = (5,6)

    with above inputs, map looks like 

      0 1 2 3 4 5 6 7 8  (S - start) 
    0 # . . . . . . . #  (T - target)
    1 . . . . . . . . .  (. - traversible coordinate)
    2 . . . . . . # . .  (# - non traversible coordinate)
    3 . S # # # # . . .  
    4 . . . . # . . . .  
    5 . . . . # . . . .  
    6 . . . . # T . . .  

    output:
    steps = 15

    ---------------------------------------------------------

    Test case 2 (target not reachable):

    input:
    map height = 7
    map width = 9
    non traversible positions: (2,3);(3,3);(4,3);(5,3);
                               (4,4);(4,5);(4,6);
                               (7,1);(6,2);(8,0);(0,0)
    start position = (1,3)
    target position = (5,6)

    with above inputs, map looks like 

      0 1 2 3 4 5 6 7 8  (S - start) 
    0 # . . . . . . . #  (T - target)
    1 . . . . . . . # .  (. - traversible coordinate)
    2 . . . . . . # . .  (# - non traversible coordinate)
    3 . S # # # # . . .  
    4 . . . . # . . . .  
    5 . . . . # . . . .  
    6 . . . . # T . . .  

    output:
    steps = -1

    ---------------------------------------------------------

    """                     
    m = Map(height=7, width=9)
    m.set_nontraversible(2, 3)
    m.set_nontraversible(3, 3)
    m.set_nontraversible(4, 3)
    m.set_nontraversible(5, 3)
    m.set_nontraversible(4, 4)           
    m.set_nontraversible(4, 5)
    m.set_nontraversible(4, 6)
    #m.set_nontraversible(7, 1)     
    m.set_nontraversible(6, 2)
    m.set_nontraversible(8, 0)
    m.set_nontraversible(0, 0)

    start = m.grid[3][1]
    rover = Rover(currentposition=start)

    target = m.grid[6][5]
    
    print(f"steps = {rover.traverse(target, m)}") 
       
if __name__ == "__main__":
    main()
