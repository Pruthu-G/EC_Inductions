from collections import deque

class Position:
    """
    This is the Position class.

    Attributes:
        x (int): takes in the x coordinate.
        y (int): takes in the y coordinate.
        is_trav (bool): True by default.
    """
    def __init__(self, x, y, is_trav = True):

        """
        Constructor for Position class.

        Parameters:
            x (int): takes in the x coordinate.
            y (int): takes in the y coordinate.
            is_trav (bool): True by default.
        """

        self.x = x
        self.y = y
        self.is_trav = is_trav

class Map:
    """
    This is the Map class.

    Attributes:
        width (int): takes in the width of the map object.
        height (int): takes in the height of the map object.
    """
    def __init__(self, width, height):

        """
        Constructor for Map class.

        Parameters:
            width (int): takes in the width of the map object.
            height (int): takes in the height of the map object.

        It takes in the height and width for the map and creates a 2D grid of the same size.
        """

        self.width = width
        self.height = height
        self.grid = [[Position(x, y) for y in range(height)] for x in range(width)]

    def get_pos(self, x, y):

        """
        This is a function to check if the position given is within the map, if yes then it returns back the grid position.

        Parameters:
            x (int): takes in x coordinate.
            y (int): takes in y coordinate.
        """

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x][y]
        return None
    
    def set_pos(self, x, y, is_trav):

        """
        This is a function to set positions which are traversable or not (by default all positions are traversable).

        Parameters:
            x (int): takes in x coordinate.
            y (int): takes in y coordinate.
            is_trav (bool): traversable or not.
        """

        pos = self.get_pos(x, y)
        if pos:
            pos.is_trav = is_trav



class Rover(Position):
    """
    This is the Rover class. Single level inheritance to Position class used for it.

    Attributes:
        x (int): takes in the initial x coordinate.
        y (int): takes in the initial y coordinate.
        battery (int): 100 by default.
    """
    def __init__(self, x, y, battery = 100):

        """
        Constructor for Rover class.

        Parameters:
            x (int): takes in the initial x coordinate.
            y (int): takes in the initial y coordinate.
            battery (int): 100 by default.
        """
        
        super().__init__(x, y, is_trav = True)
        self.battery = battery

    def trav_to(self, go_x, go_y, map):

        """
        This is the function for traversing the positions.

        Parameters:
            go_x (int): x destination.
            go_y (int): y destination.
            map (Map): Map object.

        Returns the number of steps taken if destination is traversable.
        Returns -1 if not possible.
        """
        
        if not map.get_pos(go_x, go_y).is_trav:
            return -1
        
        queue = deque()
        visited = set()
        queue.append((self.x, self.y, 0))
        visited.add((self.x, self.y))

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while queue:
            x, y, steps = queue.popleft()
            if (x==go_x and y==go_y):
                if steps > self.battery:
                    return -1
                self.battery -= steps
                self.x, self.y = go_x, go_y
                return steps
            
            for a, b in directions:
                new_x, new_y = x+a, y+b
                if 0 <= new_x < map.width and 0 <= new_y < map.height:
                    new_pos = map.get_pos(new_x, new_y)
                    if new_pos.is_trav and (new_x,new_y) not in visited:
                        visited.add((new_x,new_y))
                        queue.append((new_x, new_y, steps+1))
        return -1
    
    def __str__(self):
        return f"Rover at ({self.x}, {self.y}) with {self.battery}% battery"


# Example case.

mapObj = Map(6,6)
mapObj.set_pos(2, 0, False)
mapObj.set_pos(2, 1, False)
mapObj.set_pos(2, 2, False)
mapObj.set_pos(2, 3, False)
mapObj.set_pos(2, 4, False)

rover = Rover(0, 0)
steps = rover.trav_to(4, 2, mapObj)

print(f"Steps taken {steps}")
print(rover)
