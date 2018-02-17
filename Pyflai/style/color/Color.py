from webcolors import *


colors = dict()


class Color:
    def __init__(self, r: int, g: int, b: int, a: int = 255, name: str = None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.name = name

    def get(self) -> (int, int, int, int):
        return self.r, self.g, self.b, self.a

    def with_name(self, name: str) -> "NamedColor":
        color = NamedColor(self.r, self.g, self.b, self.a, name)
        colors[name] = color
        return color

    def no_alpha(self) -> "NoAlpha":
        return Color.NoAlpha(self.r, self.g, self.b)

    def to_string(self) -> str:
        if self.name is not None:
            return self.name
        else:
            return "No Name"

    @staticmethod
    def from_rgb(array_rgb: (int, int, int), r: int = -1, g: int = -1, b: int = -1) -> "Color":
        if array_rgb is not None:
            return Color(array_rgb[0], array_rgb[1], array_rgb[2])
        else:
            return Color(r, g, b)

    @staticmethod
    def from_rgba(array_rgba: (int, int, int, int) = None, alt_array_rgba: (int, int, int, float) = None, r: int = -1, g: int = -1, b: int = -1, alt_a: float = -1, a: int = -1) -> "Color":
        if array_rgba is not None:
            return Color(array_rgba[0], array_rgba[1], array_rgba[2], array_rgba[3])
        elif alt_array_rgba is not None:
            return Color(alt_array_rgba[0], alt_array_rgba[1], alt_array_rgba[2], alt_array_rgba[3]*255)
        else:
            return Color(r, g, b, a if a >= 0 else alt_a*255)

    @staticmethod
    def from_hex(hexadecimal: str) -> "Color":
        if not hexadecimal.startswith("#"):
            hexadecimal = "#" + hexadecimal
        return Color.from_rgb(hex_to_rgb(hexadecimal))

    @staticmethod
    def from_name(name: str) -> "NamedColor":
        return colors[name]

    class NoAlpha:
        def __init__(self, r: int, g: int, b: int):
            self.r = r
            self.g = g
            self.b = b

        def get(self) -> (int, int, int):
            return self.r, self.g, self.b


class NamedColor(Color):
    def with_name(self, name: str) -> "NamedColor":
        self.name = name
        return self
