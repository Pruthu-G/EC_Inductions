#Creating a set of classes to handle Rover in a grid based map system

"""
Position contains 3 arguments
x: x-coordinate
y: y-coordinate
is_trav: stores information on whether the grid is traversible or not
"""
class Position:
    def __init__(self, x:int, y:int, is_trav: bool=True ):
        self.x = x
        self.y = y
        self.is_trav = is_trav

"""
Map defines the a*b grid that will be formed
a: width
b: height

The set_trav method can be used to set the traversability of a grid space as on or off (true or false respectively)
"""
class Map:
    
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
        self.grid = self.get_grid()

    def get_grid(self):
        return [[Position(x, y) for x in range(self.a)]  for y in range(self.b)]                 
        
    def set_trav(self, x: int, y:int, is_trav: bool):
        if(0<=x<self.a and 0<=y<self.height):
            self.grid[y][x].is_trav = is_trav

class Rover:

    def __init__(self, s_position: Position): #takes input as start position
        self.battery = 100 #initial life is 100
        self.curr_position = s_position #sets the initial position of the rover
    def traverse(self, final_pos: Position, map: Map):
        steps = abs(final_pos.x-self.curr_position.x) + abs(final_pos.y-self.curr_position.y)
        if(steps>self.battery or not final_pos.is_trav): #checks for battery life and traversability
            return -1
        
        self.battery -= steps #deduct the battery for said amount of steps
        self.curr_position = final_pos
        return steps



        
