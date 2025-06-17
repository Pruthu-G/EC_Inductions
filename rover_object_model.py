from collections import deque

class Position:
    """
    Represents a position on the map.

    Attributes:
        x (int): The x-coordinate.
        y (int): The y-coordinate.
        traversable (bool): Indicates if the position can be traversed.
    """
    def __init__(self, x, y, traversable):
        self.x = x
        self.y = y
        self.traversable = traversable  

class Rover(Position):
    """
    Represents a rover that can move on a 2D map if enough battery is available.

    Args:
        x (int): Starting x-coordinate.
        y (int): Starting y-coordinate.
        map_data (list): The map its present in.
    """
    def __init__(self, x, y, map):
        self.map = Map(map)
        self.battery = 100
        if self.map.map[x][y] == None:
            print("Error : Coordinate not on map.")
        Position.__init__(self, x, y, True)
        

    def move_to(self, target_x, target_y):
        """
        Moves the rover to a target coordinate using the shortest path.

        Args:
            target_x (int): Target x-coordinate.
            target_y (int): Target y-coordinate.

        Returns:
            int: Number of steps taken if successful.
            str: Error message if movement is not possible.
        """
        if self.map.map[target_x][target_y] == None:
            print("Error : Can't traverse to as coordinate does not exist on map.")
            return -1
        
        if self.map.map[target_x][target_y].traversable == False:
            print("Error : The coordinate you are trying to reach is not traversable")
            return -1
        
        if self.x == target_x and self.y == target_y:
            print("rover is already here bro")
            return 0
        
        steps = self.bfs(target_x, target_y)

        if steps <= self.battery:
            self.battery = self.battery - steps
            return steps
        
        print("Not enough battery :(")
        return -1
    
    def bfs(self, target_x, target_y):
        """
        Finds the shortest path to the target using BFS.

        Args:
            target_x (int): Destination x-coordinate.
            target_y (int): Destination y-coordinate.

        Returns:
            int: Minimum steps to reach the destination.
        """
        q = deque([((self.x, self.y), 0)])
        visited = {(self.x, self.y)}

        while q:
            (x, y), steps = q.popleft()
            if (x, y) == (target_x, target_y):
                return steps

            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if (0 <= nx < 100 and 0 <= ny < 100 and self.map.map[nx][ny] and self.map.map[nx][ny].traversable and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    q.append(((nx, ny), steps + 1))


class Map():
    """
    Stores a 2D grid representation of the map with traversability info.

    Args:
        map_data (list): A list of ((x, y), traversable) tuples.
    """
    def __init__(self, map):
        self.map = [[None for _ in range(100)] for _ in range(100)]
        for coord in map:
            (x, y), traversable = coord
            self.map[x][y] = Position(x,y,traversable)


#example map
map = [[(0,2), True], [(1,2), False],[(2,2), True],
        [(0,1), False], [(1,1), True], [(2,1), True],
        [(0,0), True], [(1,0), True], [(2,0), False]]

#example usage
rov1 = Rover(0,0,map)
print(rov1.move_to(2,2)) #4
print(rov1.battery) # 96
