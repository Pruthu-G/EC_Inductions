import numpy as np
from collections import deque

class Position:
    """
    Represents a position on the map with x and y coordinates.
    
    Attributes:
        x (int): The x-coordinate.
        y (int): The y-coordinate.
        traversable (bool): Whether the position can be traversed by the rover.
    """

    def __init__(self,x,y,traversable=True):
        """
        Initializes a Position instance.

        Args:
            x (int): X-coordinate of the position.
            y (int): Y-coordinate of the position.
            traversable (bool): True if the position can be traversed.
        """
        self.x  = x
        self.y = y
        self.traversable = traversable

    def __repr__(self):
        """
        Returns a string representation of the position.
        """
        return "(x:" + str(self.x) + ",y:" + str(self.y) + ")"

class Map:
    """
    Represents the map as a 2D grid of Position objects.

    Attributes:
        width (int): Width of the map.
        height (int): Height of the map.
        grid (list of list of Position): The map grid.
    """
    def __init__(self,map_to_traverse=None):
        """
        Initializes the map from a 2D list of 1s/True (traversable) and 0s/False (blocked).

        Args:
            map_to_traverse (list of list of int): Binary matrix representing the map.
        """
        self.width = np.array(map_to_traverse).shape[1]
        self.height = np.array(map_to_traverse).shape[0]
        self.grid = [[Position(x, y, map_to_traverse[y][x] if map_to_traverse else True) for x in range(self.width)] for y in range(self.height)]
    
    def is_valid_position(self,x,y):
        """
        Checks if a given (x, y) position is within bounds and traversable.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            bool: True if the position is valid and traversable.
        """
        return 0<=x<self.width and 0<=y<self.height and self.grid[y][x].traversable

    def get_position(self,x,y):
        """
        Returns the Position object at (x, y) if valid, otherwise None.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            Position or None: The Position object if valid, else None.
        """
        return self.grid[y][x] if self.is_valid_position(x,y) else None




class Rover:
    """
    Represents a Rover that can traverse a Map.

    Attributes:
        battery (int): Battery percentage (starts at 100).
        cur_pos (Position): The current position of the rover.
        total_steps (int): Total number of steps taken so far.
    """
    battery = 100

    def __init__(self , cur_pos):
        """
        Initializes the rover at a starting position.

        Args:
            cur_pos (Position): The starting position of the rover.
        """
        self.cur_pos = cur_pos
        self.total_steps = 0

    def get_info(self):
        """
        Prints information about the rover.
        """
        print("Remaining battery(%):",self.battery)
        print("Current position:",self.cur_pos)
        print("Total distance traveled:",self.odometer(),"\n")


    def odometer(self):
        """
        Returns the total number of steps taken by the rover.

        Returns:
            int: Total steps taken.
        """
        return self.total_steps
    
    def traverse(self,target_pos,map_obj):
        """
        Attempts to traverse from the current position to a target position.
        
        The rover can only move non-diagonally and consumes 1% battery per step.

        Args:
            target_pos (Position): The destination position.
            map_obj (Map): The map object to traverse.

        Returns:
            int: Number of steps taken if successful, -1 otherwise.
        """
        if target_pos is None:
            return -1
        starting_pos = self.cur_pos
        visited = set()
        to_visit = deque([(starting_pos.x,starting_pos.y,0)])
        
        dir = [(1,0) , (0,1) , (-1,0) , (0,-1)]

        while to_visit:
            x,y,steps = to_visit.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))

            if (x,y) == (target_pos.x,target_pos.y):
                if steps <= self.battery:
                    self.battery -= steps
                    self.cur_pos = map_obj.get_position(x,y)
                    self.total_steps += steps
                    return steps
                else:
                    return -1

            for i,j in dir:
                new_x , new_y = x+i , y+j
                if map_obj.is_valid_position(new_x,new_y) and (new_x,new_y) not in visited:
                    to_visit.append((new_x,new_y,steps+1))

            
        return -1

if __name__ == '__main__':

    traversable_map = [
        [1, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ]

    my_map = Map(traversable_map)
    rover = Rover(my_map.get_position(0,0))

    target = my_map.get_position(3,2)

    print("Steps taken:",rover.traverse(target, my_map))
    rover.get_info()


    target = my_map.get_position(2,1)

    print("Steps taken:",rover.traverse(target, my_map))
    rover.get_info()


    target = my_map.get_position(1,1)

    print("Steps taken:",rover.traverse(target, my_map))
    rover.get_info()

    
