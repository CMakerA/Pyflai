from Pyflai.style.color import *
from Pyflai.style.font import *
from Pyflai.style.style.BorderStyle import *


class SingleStyle:
    def __init__(self, background_color: Color, border_style: BorderStyle, font: Font, selection_color: Color, name: str = None):
        self.background_color = background_color
        self.border_style = border_style
        self.font = font
        self.selection_color = selection_color
        self.name = name

    def clone(self) -> "SingleStyle":
        return SingleStyle(self.background_color, self.border_style, self.font, self.selection_color, self.name)

    def with_background_color(self, background_color: Color) -> 'SingleStyle':
        self.background_color = background_color
        return self

    def with_border_style(self, border_style: BorderStyle) -> 'SingleStyle':
        self.border_style = border_style
        return self

    def with_border_color(self, border_color: Color) -> 'SingleStyle':
        self.border_style.color = border_color
        return self

    def with_border_width(self, border_width: int) -> 'SingleStyle':
        self.border_style.width = border_width
        return self

    def with_font(self, font: Font) -> 'SingleStyle':
        self.font = font
        return self

    def with_font_color(self, font_color: Color) -> 'SingleStyle':
        self.font.color = font_color
        return self

    def with_font_size(self, font_size: int) -> 'SingleStyle':
        self.font.color = font_size
        return self

    def with_selection_color(self, selection_color: Color) -> 'SingleStyle':
        self.selection_color = selection_color
        return self

    def with_name(self, name: str) -> 'SingleStyle':
        self.name = name
        return self


class Style:
    def __init__(self, idle_style: SingleStyle, clicked_style: SingleStyle, right_clicked_style: SingleStyle,
                 hovered_style: SingleStyle, focused_style: SingleStyle, name: str = None):
        self.idle_style = idle_style
        self.clicked_style = clicked_style
        self.right_clicked_style = right_clicked_style
        self.hovered_style = hovered_style
        self.focused_style = focused_style
        self.name = name
