class Position:
    '''Creating constructor for Position class that take integer Coordinates and whether point
        is traversable or not.'''
    def __init__(self, x_cord: int ,y_cord : int ,trav :bool=True):
        self.x=x_cord;
        self.y=y_cord;
        self.traversable=trav

class Map:
    """ creating constructor for Map class with start and end positions
        A rectangular map will be created with start and end points as opposite sides"""
    def __init__(self,start_pos:Position , end_pos:Position):
        self.arr=[]
        self.columns=abs(end_pos.x-start_pos.x)+1
        self.rows=abs(end_pos.y-start_pos.y)+1
        for numy in range(start_pos.y,end_pos.y+1):
            row_arr=[]
            for numx in range(start_pos.x,end_pos.x+1):
                row_arr.append(Position(numx,numy))
            self.arr.append(row_arr)
        '''Here I used 2D list that contains Position objects'''

class Rover:
    ''' constructor for Rover class'''
    def __init__(self,bat,cur_pos:Position):
        Rover.battery=bat
        Rover.cur_pos=cur_pos

    def traversable(self,end_pos:Position,map:Map)->int:
        ''' Checking wheter start and end postitions are in map'''
        if(self.cur_pos not in map.arr or end_pos not in map.arr): return -1

        steps=0
        steps+=abs(end_pos.x-self.cur_pos.x)
        steps+=abs(end_pos.y-self.cur_pos.y)
        ''' returning -1 if steps are greater than 100 as battery will be drained in that case'''
        if(steps>100): return -1
        else: return steps
