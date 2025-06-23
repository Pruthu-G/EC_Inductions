import random
class Position:
    def __init__(self, x, y, traversable):
        self.x = x
        self.y = y
        self.traversable = traversable

class Map:
    def __init__(self):
        self.m = 10
        self.n = 10
        self.grid = []
        for i in range(self.m):
            a = [0] * self.n
            self.grid.append(a)
        for i in range(self.m):
            for j in range(self.n):
                a = random.random()
                if a > 0.8:
                    b = False
                else:
                    b = True
                self.grid[i][j] = Position(i, j, b)
    
    def is_traversable(self, x, y):
        if 0 <= x < self.m and 0 <= y < self.n:
            return self.grid[x][y].traversable
        return False

class Rover:
    def __init__(self, position, map):
        self.battery = 100
        self.position = position
        self.map = map
    def move(self):       
        target = [5, 5]
        moved = []
        moved.append([self.position.x, self.position.y])
        count = 0
        stuck = 0
        while (self.battery > 0):
            a = random.random()
            if ((a < 0.25 and self.position.x < 10) and ([self.position.x+1, self.position.y] not in moved)):
                if (self.map.is_traversable(self.position.x+1, self.position.y)):
                    self.position.x += 1
                    count += 1
                    moved.append([self.position.x, self.position.y])
                    self.battery -= 1
                    stuck = 0
                else:
                    stuck+=1
            elif ((0.5 > a >= 0.25 and self.position.x > 0) and ([self.position.x-1, self.position.y] not in moved)):
                if (self.map.is_traversable(self.position.x-1, self.position.y)):
                    self.position.x -= 1
                    count+=1
                    moved.append([self.position.x, self.position.y])
                    self.battery -= 1
                    stuck = 0
                else:
                    stuck+=1
            elif ((0.75 > a >= 0.5 and self.position.y < 10) and ([self.position.x, self.position.y+1] not in moved)):
                if (self.map.is_traversable(self.position.x, self.position.y+1)):
                    self.position.y += 1
                    count+=1
                    moved.append([self.position.x, self.position.y])
                    self.battery -= 1
                    stuck = 0
                else:
                    stuck+=1
            elif ((1.00 >= a >= 0.75 and self.position.y > 0) and ([self.position.x, self.position.y-1] not in moved)):
                if (self.map.is_traversable(self.position.x, self.position.y-1)):
                    self.position.y -= 1
                    count+=1
                    moved.append([self.position.x, self.position.y])
                    self.battery -= 1
                    stuck = 0
                else:
                    stuck+=1

            if ([self.position.x, self.position.y] == target):
                return count
                break
            
            if (stuck > 15):
                print("No possible moves left. Stopping.")
                return -1
            
        return -1