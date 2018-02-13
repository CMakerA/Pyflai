from drawing import *
from dimensions import *
from ui.UIElement import *
from style.font import *
import pygame


class Label(UIElement):
    def __init__(self, position: Position, text: str, font: Font):
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

    def update(self):
        self.instance = self.font.get().render(self.text, 1, self.font.color.get())

    def draw(self):
        if self.screen is not None:
            self.screen.blit(self.instance, self.position.get())
