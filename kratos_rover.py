

class Position:
    """
    
    Position specifies the x and y coordinates of a certain position,
and should also hold information about whether the particular coordinate is
traversable or not.

    Attributes:
        x: Row index
        y: Column index
        traversable: 1 = traversable, 0 = not traversable
     """
    def __init__(self, x, y, traversable=1):
        self.x = x
        self.y = y
        self.traversable = traversable
