from Pyflai.dimensions.Vector2 import *


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

    def get(self) -> (int, int, int, int):
        return self.vector1.x, self.vector1.y, self.vector2.x, self.vector2.y

    def to_string(self) -> str:
        return "(" + str(self.vector1.x) + ", " + str(self.vector1.y) + ", " + str(self.vector2.x) + ", " + str(self.vector2.y) + ")"

    def point_over(self, point: Vector2) -> bool:
        return self.vector1.x < point.x < self.vector2.x and self.vector1.y < point.y < self.vector2.y
