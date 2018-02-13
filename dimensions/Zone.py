from dimensions.Vector2 import *


class Zone:
    def __init__(self, vector1: Vector2, vector2: Vector2 = None):
        """Instantiate a Zone class.
        If vector2 is not specified, vector2 will be vector1.

        Keyword arguments:
        vector1 -- The first vector to store : Vector2
        vector2 -- The second vector to store (optional) : Vector2
        """
        self.vector1 = vector1
        if vector2 is None:
            self.vector2 = vector1
        else:
            self.vector2 = vector2

    def get(self):
        return self.vector1.x, self.vector1.y, self.vector2.x, self.vector2.y
