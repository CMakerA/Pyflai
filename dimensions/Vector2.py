class Vector2:
    def __init__(self, x: int, y: int = -1):
        """Instantiate a Vector2 class.
        If y is not specified, y will be x.

        Keyword arguments:
        x -- The x variable : int
        y -- The y variable (optional) : int
        """
        self.x = x
        if y < 0:
            self.y = x
        else:
            self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def get(self) -> (int, int):
        return self.x, self.y
