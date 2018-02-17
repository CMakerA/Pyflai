from Pyflai.drawing import *
from Pyflai.dimensions import *
from Pyflai.ui.UIElement import *
from Pyflai.style.font import *
from Pyflai.style.color import *
import pygame


class Label(UIElement):
    def __init__(self, position: Position, text: str, font: Font = Fonts.default):
        super().__init__("Label", Size(0, 0), position)
        pygame.font.init()
        self.text = text
        self.font = font
        self.instance = self.font.get().render(self.text, 1, self.font.color.get())

    def with_text(self, text: str) -> "Label":
        self.text = text
        return self

    def with_font(self, font: Font) -> "Label":
        self.font = font
        return self

    def with_font_size(self, size: int) -> "Label":
        self.font.size = size
        return self

    def with_font_color(self, color: Color) -> "Label":
        self.font.color = color
        return self

    def update(self):
        self.instance = self.font.get().render(self.text, 1, self.font.color.get())

    def get_instance(self, text: str = None, font: Font = None):
        if str is None and font is not None:
            return font.get().render(self.text, 1, font.color.get())
        elif str is not None and font is None:
            return self.font.get().render(text, 1, self.font.color.get())
        elif str is None and font is None:
            return self.font.get().render(self.text, 1, self.font.color.get())
        else:
            return font.get().render(text, 1, font.color.get())

    def draw(self):
        if self.screen is not None:
            self.screen.blit(self.get_instance(), self.position.get())

    def clear(self):
        if self.screen is not None:
            self.screen.blit(self.get_instance(font=self.font.with_color(self.window.background_color)),
                             self.position.get())
