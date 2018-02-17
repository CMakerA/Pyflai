from Pyflai.dimensions.Percentage import *


class Vector2:
    def __init__(self, x: int = -1, y: int = -1, altx: perc = None, alty: perc = None):
        """Instantiate a Vector2 class.
        If y is not specified, y will be x.

        Keyword arguments:
        x -- The x variable : int
        y -- The y variable (optional) : int
        altx -- The x variable as a percentage of the main container : perc
        alty -- The y variable as a percentage of the main container (optional) : perc
        """
        if x >= 0:
            self.x = x
            self.y = x if y < 0 else y
            self.altx = None
            self.alty = None
        else:
            self.x = -1
            self.y = -1
            self.altx = altx
            self.alty = altx if alty is None else alty

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def get(self) -> (int, int):
        return self.x, self.y
