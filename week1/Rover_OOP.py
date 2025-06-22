class Position(object):
    def __init__(self, x: int, y: int, traversable: bool):
        """Initializing the Position class
        Parameters :
            x (int) : x position
            y (int) : y position"""
        self.x = x
        self.y = y
        self.traversable = traversable


class Map(object):
    def __init__(self, x_min, x_max, y_min, y_max):
        """Initializing the Map class
        Parameters :
            x_min, x_max, y_min, y_max (int) : self explanatory"""
        self.grid_list = []
        for a in range(x_min, x_max + 1):  # Nested for loop to create tuples with all positions
            temp_list = []
            for b in range(y_min, y_max + 1):
                temp_list.append(Position(a, b, True))
            self.grid_list.append(temp_list)


class Rover(object):
    def __init__(self, x_init, y_init, battery_init):
        """Initializing the Rover class
        Parameters :
            x_init,y_init (int) : starting position
            battery_init (int) : 0 to 100 in %"""
        self.pos = Position(x_init, y_init, True)
        self.battery = battery_init

    def travel(self, x_dest, y_dest, map_in, steps=0):
        """Travel using recursive function"""
        if self.battery > 0:
            self.battery -= 1
            print("x:", self.pos.x, " y:", self.pos.y, " steps:", steps)
            if self.pos.x != x_dest:
                self.pos.x += int(abs(x_dest - self.pos.x) / (x_dest - self.pos.x))  # This expression travels the map by 1 unit
                return self.travel(x_dest, y_dest, map_in, steps + 1)
            elif self.pos.y != y_dest:
                self.pos.y += int(abs(y_dest - self.pos.y) / (y_dest - self.pos.y))
                return self.travel(x_dest, y_dest, map_in, steps + 1)
            else:
                return steps
        else:
            return -1


r1 = Rover(2, 2, 100)
print(r1.travel(100, 0))
