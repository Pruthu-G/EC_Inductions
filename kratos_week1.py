class Position:
    '''Defines X and Y coordinates for the rover'''
    def __init__(self, x, y):
        self.x= x
        self.y = y
        

class Map:
    '''Makes a boundary for the rover outside which position is not valid'''
    def __init__ (self, length, width):
        self.length= length
        self.width= width

    def valid_posn (self, x, y):
        '''Check validity of position'''
        return ((x>=0) and (x< self.length) and (y>=0) and (y<self.width) )
    

class Rover:
    def __init__ (self, x_posn, y_posn, map_obj, battery=100):
        '''Rover class with position, battery and map'''
        self.battery= battery
        self.x_posn= x_posn
        self.y_posn= y_posn
        self.map= map_obj

    def move(self, targ_x, targ_y):
        '''This is the target position. '''
        self.targ_x= targ_x
        self.targ_y= targ_y
        '''Check for validity on the map'''
        if not self.map.valid_posn(targ_x, targ_y):
            return -1
        '''Count steps.'''
        steps= abs(targ_x- self.x_posn) + abs(targ_y-self.y_posn)
        '''Not valid if the position more than hundred steps as we lose 1 percent with each step'''
        if self.battery< steps:
            return -1
        '''Update battery and current position'''
        self.battery=- steps 
        self.x_posn= targ_x
        self.y_posn= targ_x

        
    def move (self, targ_x, targ_y):

        '''Move in X and Y direction one step at a time'''
        if (self.targ_x> self.x_posn):
            step_x= 1
        else :
            step_x= -1

        if targ_y> self.y_posn:
            step_y= 1
        else :
            step_y= -1
   

        while (self.x_posn!= targ_x) :
            self.x_posn+= step_x
            self.battery=- 1

        while (self.y_posn!= targ_y) :
            self.y_posn_posn+=step_y
            self.battery=- 1

        return abs(targ_x- self.x_posn) + abs(targ_y-self.y_posn)
    
    

        