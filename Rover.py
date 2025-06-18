import numpy as np
class Position:
    """
    This is a class which contains variables for coordinates
    Attributes:
        x : the x-coordinate on the terrain
        y : the y-coordinate on the terrain
        traverse : Specifies whether the rover can travel upto the afore-mentioned (x,y).
    """
    def __init__(self,x,y):
        """
        Initialises a Position object
        Parameters:
            x : an integer which is the x-coordinate
            y : an integer which is the y-coordinate
            traverse : a boolean variable which tells whether the rover can travel to (x,y) or not.
        """
        self.x_=x
        self.y=y
        self.traverse=True
help(Position)

class Map:
    """
    This is a class which creates the map of the terrain containing those coordinates the rover can access
    Attributes:
        x_initial : The very first x coordinate the rover has when it's battery is 100%
        y_initial : The very first y coordinate the rover has when it's battery is 100%
        my_map : A map of all the possible x and y coordinates the rover can go to.
    """
    def __init__(self,x_initial,y_initial):
        """
        Initialises a map object
        Parameters:
            x_initial : An integer which is the rover's initial x-coordinate
            y_initial : An integer which isth e rover's initial y-coordinate
            my_map : A 2-D array which consist of the range of x and y coordinates the rover accesses.
        """
        self.x_initial=x_initial
        self.y_initial=y_initial
        self.my_map=np.array([[num for num in range(x_initial-100,x_initial+101)],[num for num in range(y_initial-100,y_initial+101)]])
        #print(self.my_map)
    
help(Map)
x_initial=int(input("Enter starting x coordinate : "))
y_initial=int(input("Enter starting y coordinate : "))

my_map=Map(x_initial,y_initial)
x_current=x_initial
y_current=y_initial

current_pos=Position(x_current,y_current)
#

class Rover:
    """
    This class contains an object using the "Position" class and the battery percentage remaining with the rover
    Attributes:
        current_pos : The current coordinate of the rover
        batter_life : The remaining percentage of battery left with the rover.
    """
    def __init__(self,current_pos,battery_life=100,):
        """
        Initialises a rover object
        Parameters:
            current_pos : A position object which specifies the rover's current position
            battery_life : An integer which has been set to 100 since the first time the rover
            moves, its battery is 100%.
        """
        self.battery_life=battery_life
        self.current_pos=current_pos
        

    def traversability(x_new,y_new,current_pos,battery_life):
        """
        Determines whether the rover can traverse to a desired coordinate using the shortest possible route
        Parameters:
            x_new,y_new : The desired new integer coordinates of the rover
            current_pos : A position object of the rover's current position
            battery_lfe : Remaining battery of the rover

        If the rover can move to the new position, it updates the rover's coordinates, as well as the battery life
        It sets the traverse variable to True, counts the number of steps required and returns them

        If the rover doesn't have as much battery so as to reach the new destination, it returns -1.
        """
        
        if(battery_life-abs(x_new-current_pos.x)-abs(y_new-current_pos.y)>=0):
            current_pos.y=x_new
            current_pos.y=y_new
            battery=battery_life-abs(x_new-current_pos.x)-abs(y_new-current_pos.y)
            num_steps=abs(x_new-current_pos.x)+abs(y_new-current_pos.y)
            current_pos.traverse=True
            #print(current_pos.traverse)
            #print(num_steps)
            return num_steps
        else:
            current.traverse=False
            return -1    
help(Rover)
           
    
