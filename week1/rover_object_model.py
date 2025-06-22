"""
Rover Navigation Model (Week 1 Assignment)
------------------------------------------

This Python module provides an object-oriented model of a rover navigating on a map grid.
1. Define a `Position` class to store:
    - (x, y) coordinates
    - Whether the position is traversable or not

2. Define a `Map` class that:
    - Represents a grid (2D array) of `Position` objects
    - Provides access to positions by coordinates

3. Define a `Rover` class with:
    - Properties:
        - `battery`: starts at 100%
        - `current_position`: a `Position` object indicating current location
    - Method:
        - `traverse_to(target_x, target_y)`:
            - Moves the rover from its current position to a target position on the map
            - Only non-diagonal (up, down, left, right) steps are allowed
            - Returns the number of steps taken if successful
            - Consumes 1% battery per step
            - Returns -1 if:
                - The destination is unreachable
                - There is not enough battery to complete the trip """

from collections import deque
class Position:
    def __init__(self,x,y,traversability):
        self.x = x
        self.y = y
        self.traversability = traversability # 1 = not traversable, 0 = traversable

class Map:
    def __init__(self,traverse_matrix):
        self.traverse_matrix = traverse_matrix
        self.matrix = [[Position(x,y,traverse_matrix[x][y])for y in range(len(traverse_matrix[0]))]for x in range(len(traverse_matrix))]

    def getpos(self,x,y):
        return self.matrix[x][y]    

class Rover:
    def __init__(self,battery_life,x,y,map):
        self.battery_life = battery_life
        self.current_pos = map.getpos(x,y)
    
    def traverse(self,end_x,end_y):
        if self.current_pos.traversability:
            return -1
        endpos = map.getpos(end_x,end_y)
        if not endpos or not endpos.traversability:
            return -1
        
        visited = [[False]*range(len(self.matrix[0]))for _ in range(len(self.matrix))]
        queue = deque()    
        queue.append((self.current_pos.x,self.current_pos.y,0)) #x,y and steps taken
        visited[self.current_pos.x][self.current_pos.y] = True

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            x, y, steps = queue.popleft()
            if(x==end_x and y==end_y):
                if steps >= self.battery_life:
                    steps-= self.battery_life
                    return steps
                else:
                    return -1
       
            for dx,dy in directions:
                nx = x+dx
                ny=y+dy
                next_pos = self.map.getpos(nx,ny)
                if next_pos and next_pos.traversability and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append(nx,ny,steps+1)

        return -1                    