from drawing import *
from dimensions import *
from ui.UIElement import *
from style.font import *
from ui.elements.Label import *
import pygame
from drawing import *
from style.style import *


class Button(UIElement):
    # TODO: Change style depending on status: Idle, Click, Hover

    def __init__(self, position: Position, size: Size, text: str, style: Style = Styles.button):
        super().__init__("Button", size, position)
        pygame.font.init()
        self.text = text
        self.font = style.font
        self.style = style
        self.label = Label(position, text, style.font)

    def with_size(self, size: Size) -> "Button":
        self.size = size
        return self

    def with_position(self, position: Position) -> "Button":
        self.position = position
        return self

    def with_text(self, text: str) -> "Button":
        self.text = text
        return self

    def with_font(self, font: Font) -> "Button":
        self.font = font
        return self

    def update(self):
        self.label = Label(self.position, self.text, self.font)

    def draw(self):
        Helper.draw_rounded_rect(self.zone, self.style.border_style.color, self.screen)
        self.label.draw()
