import pygame.font
from Pyflai.style.color import *
from Pyflai.system.filesystem import *


class Font:
    def __init__(self, name: str, size: int = 15, color: Color = Color(0, 0, 0), bold: bool = False, italic: bool = False):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.color = color

    def with_name(self, name: str) -> 'Font':
        self.name = name
        return self

    def from_file(self, file: File) -> 'Font':
        self.name = file.path
        return self

    def with_size(self, size: int) -> 'Font':
        self.size = size
        return self

    def set_bold(self, bold: bool) -> 'Font':
        self.bold = bold
        return self

    def set_italic(self, italic: bool) -> 'Font':
        self.italic = italic
        return self

    def with_color(self, color: Color) -> 'Font':
        self.color = color
        return self

    def get(self) -> pygame.font:
        return pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
