from collections import deque

class Position:
    '''
    Position:
    Specifies the x and y coordinates of a certain position and holds information about whether it is traversable or not.
    x : x-coordinate of rover.
    y : y-coordinate of rover.
    traversable : boolean which returns if rover is traversable across that point.
    '''
    def __init__(self, x, y, traversable):
        self.x = x
        self.y = y
        self.traversable = traversable

class Map:
    '''
    Map:
    Grid of points (2D arrays).
    width : width of map.
    height : height of map.
    traversable_matrix : nested list of points which are traversable and non traversable in the form of boolean values.
    '''
    def __init__(self, width, height, traversable_matrix):
        self.grid = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(Position(j, i, traversable_matrix[i][j]))
            self.grid.append(row)
    
    '''
    Returns the position of rover on the map.
    '''
    def get_position(self, x, y):
        return self.grid[y][x]


class Rover:
    '''
    Rover:
    battery_life : Initialised at 100 and decrements by 1 for each move the rover makes.
    current : Real-time current position of rover
    '''
    def __init__(self, current):
        self.battery_life = 100
        self.current = current

    '''
    BFS search to find the fastest way to final position.
    Searched up different methods to optimise the process of reaching the final point using graph theory in google and I decided to go with BFS as it is simplest for navigating.
    A* could be similary used for the same but since it requires a heuristic approach, I decided to go with the below code which is the algorithm for BFS as it is more hard coded.
    '''

    def traverse(self, target_position, map_obj):
        width = len(map_obj.grid[0])
        height = len(map_obj.grid)
        visited = [[False]*width for _ in range(height)] # visited : A matrix which resembles the Map. It is initially set to False.
        queue = deque()
        queue.append((self.current.x, self.current.y, 0))
        visited[self.current.y][self.current.x] = True # When the rover passes a point, that point is set to True.


        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == (target_position.x, target_position.y):
                if steps > self.battery_life:
                    return -1
                self.battery_life -= steps
                self.current_position = Position(x, y, True)
                return steps
            #BFS Code snippet
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < width and 0 <= ny < height:
                    if not visited[ny][nx] and map_obj.grid[ny][nx].traversable:
                        visited[ny][nx] = True
                        queue.append((nx, ny, steps+1))
        return -1