import numpy as np
import math
import sys
class Position:
    """
    Represents a single cell on the map.
    Stores its (x, y) coordinates and whether it is traversable (0) or an obstacle (1).
    """
    def __init__(self, x, y, is_traversable):
        self.x=x
        self.y=y
        self.is_traversable = (is_traversable==0)
        
class Map:
    """
    Represents a 2D grid map composed of Position objects.
    Each Position is initialized based on the input grid of 0s (traversable) and 1s (obstacles).
    """
    def __init__(self, w, h, v):
        self.w=w
        self.h=h
        self.grid = [[Position(x, y, v[y][x]) for x in range(w)] for y in range(h)]
    def display(self):
        """
        Randomly generates a grid using numpy made up of 1s and 0s where 0 represents traversable area
        whereas 1 represent non traversable area
        """
        for row in self.grid:
            print(' '.join('0' if pos.is_traversable else '1' for pos in row))



class Rover:
    """
    Simulates a rover with a current position and battery life.
    Can move to adjacent cells and traverse to a destination using BFS.
    """
    def __init__(self, start_position):
        self.current_position = start_position
        self.battery = 100

    def move_to(self, new_position):
        """
        Attempts to move the rover to a new traversable position.
        Reduces battery by 1% if successful.
        """
        if new_position.is_traversable and self.battery > 0:
            self.current_position = new_position
            self.battery -= 1
            return True
        return False

    def status(self):
        """
        Returns the current status of the rover including its position and battery level.
        """
        return f"Rover at ({self.current_position.x}, {self.current_position.y}), battery: {self.battery}%"

    def traverse_to(self, target_x, target_y, map_obj):
        """
        Uses Breadth-First Search (BFS) to find the shortest path to the target position.
        If a path is found, moves the rover step-by-step along that path.
        Returns True if the destination is reached, False otherwise.
        """
        from collections import deque
        start = (self.current_position.x, self.current_position.y)
        goal = (target_x, target_y)

        queue = deque()
        queue.append((start, []))
        visited = set()

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            path = path + [(x, y)]

            if (x, y) == goal:
                for step_x, step_y in path[1:]:
                    self.move_to(map_obj.grid[step_y][step_x])
                return True

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < map_obj.w and 0 <= ny < map_obj.h:
                    neighbor = map_obj.grid[ny][nx]
                    if neighbor.is_traversable and (nx, ny) not in visited:
                        queue.append(((nx, ny), path))
        return False


"""
Main Execution:
1. Generate a random 50x50 grid with 0.8 probability of traversable cells.
2. Construct the map and display it.
3. Create a rover at the start position (0, 0).
4. Ask user for destination coordinates.
5. Use BFS to attempt a full traversal to that location.
6. Print the final result and rover status.
"""
grid_data = np.random.choice([0, 1], size=(50, 50), p=[0.8, 0.2]).tolist()
# print(f"Grid shape: {len(grid_data)} rows x {len(grid_data[0])} cols")
# for y in range(len(grid_data)):
#     for x in range(len(grid_data[y])):
#         print(f"grid_data[{y}][{x}] = {grid_data[y][x]}")

my_map = Map(50, 50, grid_data)
my_map.display()
start_pos = my_map.grid[0][0]
rover = Rover(start_pos)

# Show final rover status after displaying the map
print("Final Rover Status:")
print(rover.status())
a, b = map(int, input("Where do you want to direct the rover? (x y): ").split())
if((a>50)|(b>50)):
    print("Rover is outside the map")
    sys.exit()
print(f"\nAttempting full traversal to ({a}, {b}):")
success = rover.traverse_to(a, b, my_map)
print("Traversal success:", success)
print("Final Rover Status:")
print(rover.status())