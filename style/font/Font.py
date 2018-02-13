import pygame.font
from style.color import *


class Font:
    def __init__(self, name: str, size: int = 15, color: Color = Color(0, 0, 0), bold: bool = False, italic: bool = False):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.color = color

    def with_size(self, size: int) -> 'Font':
        return Font(self.name, size, self.color, self.bold, self.italic)

    def set_bold(self, bold: bool) -> 'Font':
        return Font(self.name, self.size, self.color, bold, self.italic)

    def set_italic(self, italic: bool) -> 'Font':
        return Font(self.name, self.size, self.color, self.bold, italic)

    def with_color(self, color: Color) -> 'Font':
        return Font(self.name, self.size, color, self.bold, self.italic)

    def get(self) -> pygame.font:
        return pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
