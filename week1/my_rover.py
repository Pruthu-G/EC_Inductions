from typing import List
from collections import deque
from typing import Tuple, Dict, List, Optional


class Position:
    def __init__(self, x: int, y: int, traversable: bool):
        
        
        """
        Initialize the Position class for a rover.

        Args:
            x (float): _x-coordinate of the rover._
            y (float): y-coordinate of the rover.
            traversable (bool): determins if the rover can traverse the position 
                                (used later when creating a list of booleans in class Map).
                                
        """
        self.x = x
        self.y = y
        self.traversable = traversable
        
    
    def __where__(self):
        
        """
        Return the position of the rover.
        
        Parameters:
            x(int): The x-coordinate of the rover.
            y(int): The y-coordinate of the rover.
            
        Returns:
            str: A string representation of the rover's position.
        """

        return f"Position({self.x}, {self.y})"
    
    
    def is_traversable(self) -> bool:
        """
        Return True if this cell itself allows traversal.
        (No bounds‐checking here — Position doesn’t know the map size.)
        """
        return self.traversable
    
    
class Map:
    """
    im assuming height and width of the grid are given, not the number of pts on X and Y axes resp
    
    """
    def __init__(self,
                 width: int,
                 height: int,
                 initial_grid: List[List[bool]]):
        """
        Create a Map of given width×height.

        Args:
            width (int):  number of columns (x‑span).
            height (int): number of rows    (y‑span).
            initial_grid (List[List[bool]]): 
                A 2D list of booleans, True if that cell is traversable.
        """
        self.width = width
        self.height = height
        
        # Check number of rows
        if len(initial_grid) != height:
            raise ValueError(f"initial_grid must have {height} rows, got {len(initial_grid)}")

        # Check each row’s length
        for row_idx, row in enumerate(initial_grid):
            if len(row) != width:
                raise ValueError(f"Row {row_idx} must have {width} columns, got {len(row)}")
            
        # Create a grid of Position objects
        self.grid = [
            [
                Position(x, y, initial_grid[y][x]) # Note that the position according to the 2D-grid is (y,x)
                for x in range(width)             #range is inclusive of the start and exclusive of the end
            ]
            for y in range(height)
        ]
        
    def is_traversable(self, x: int, y: int) -> bool:
        
        """Check if the position (x, y) is traversable.
        
        Args:
            x (int): The x-coordinate of the position to check.
            y (int): The y-coordinate of the position to check.

        Returns:
            bool: First checks if the coordinates are within the bounds of the map,
                  then checks if the position itself is traversable.
        """
        
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.grid[y][x].traversable




def bfs_path(map_obj: Map,
             start: Tuple[int, int],
             goal: Tuple[int, int]
            ) -> Optional[List[Tuple[int, int]]]:
    """
    Use BFS to find the shortest path (grid moves) from start to goal.

    Returns:
        A list of (x, y) coordinates including start and goal
        – or None if no path exists.
        
    IDK how the code actually works, I just copied it as is.
    """
    queue = deque([start])
    parent: Dict[Tuple[int,int], Tuple[int,int]] = {}
    visited = {start}
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            path = []
            node = goal
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            return list(reversed(path))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and map_obj.is_traversable(nx, ny):
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return None





class Rover:
    def __init__(self, start_pos: Position, map_obj: Map):
        """
        Initialize the rover.

        Args:
            start_pos (Position): Starting location for the rover.
            map_obj (Map): The map instance the rover navigates.

        Raises:
            ValueError: If the starting position is blocked (non-traversable).
        """
        if not start_pos.is_traversable():
            raise ValueError("Starting position is blocked.")
        self.battery = 100
        self.position = start_pos

    def compute_steps_to(self, target_pos: Position, map_obj: Map) -> Tuple[int, Optional[List[Tuple[int, int]]]]:
        """
        Plan a path from the current position to a target using BFS.

        Args:
            target_pos (Position): Desired destination position.
            map_obj (Map): Map object for bounds and traversability checks.

        Returns:
            steps (int): Number of steps required (excluding the starting cell).
                         Returns -1 if the path is unreachable or exceeds battery.
            path (List[Tuple[int, int]] | None): Coordinates of the planned route,
                         including start and goal; None if planning failed.
        """
        # Ensure the goal is valid and free
        if not map_obj.is_traversable(target_pos.x, target_pos.y):
            return -1, None

        start_coords = (self.position.x, self.position.y)
        goal_coords = (target_pos.x, target_pos.y)

        path = bfs_path(map_obj, start_coords, goal_coords)
        if path is None:
            return -1, None

        steps_needed = len(path) - 1
        if steps_needed > self.battery:
            return -1, None

        return steps_needed, path

    def execute_traverse(self, target_pos: Position, map_obj: Map) -> bool:
        """
        Execute movement along a pre-planned path.

        Args:
            target_pos (Position): The target position to reach.
            map_obj (Map): Map object to retrieve Position instances.

        Returns:
            bool: True if movement succeeded (path existed and battery sufficient);
                  False otherwise.
        """
        steps, path = self.compute_steps_to(target_pos, map_obj)
        if steps == -1 or path is None:
            return False  # Cannot move

        # Move step-by-step, updating position and decrementing battery
        for x, y in path[1:]:
            self.position = map_obj.grid[y][x]
            self.battery -= 1

        return True





"""I sent my code to Chat GPT and asked it to create a test case for it.

if __name__ == "__main__":
    # Example grid: 5x5 grid, all True (traversable)
    initial_grid = [[True for _ in range(5)] for _ in range(5)]

    # Create map and start/goal positions
    map_obj = Map(5, 5, initial_grid)
    start_pos = map_obj.grid[0][0]  # Top-left corner
    goal_pos = map_obj.grid[4][4]   # Bottom-right corner

    rover = Rover(start_pos, map_obj)

    steps, path = rover.compute_steps_to(goal_pos, map_obj)
    print("Planned Steps:", steps)
    print("Path:", path)

    if rover.execute_traverse(goal_pos, map_obj):
        print("Rover successfully moved.")
        print("Current Position:", rover.position.__where__())
        print("Remaining Battery:", rover.battery)
    else:
        print("Rover failed to reach destination.")

"""