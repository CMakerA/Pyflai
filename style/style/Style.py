from style.color import *
from style.font import *
from style.style.BorderStyle import *


class Style:
    def __init__(self, background_color: Color, hover_background_color: Color, click_background_color: Color,
                 focused_background_color: Color,
                 border_color: Color, hover_border_color: Color, click_border_color: Color, focused_border_color: Color,
                 border_width: int, hover_border_width: int, click_border_width: int, focused_border_width: int,
                 font: Font, hover_font: Font, click_font: Font, focused_font: Font,
                 text_color: Color, hover_text_color: Color, click_text_color: Color, focused_text_color: Color,
                 text_size: int,
                 selection_text_color: Color, selection_mark_color: Color):
        self.background_color = background_color
        self.hover_background_color = hover_background_color
        self.click_background_color = click_background_color
        self.focused_background_color = focused_background_color
        self.border_color = border_color
        self.hover_border_color = hover_border_color
        self.click_border_color = click_border_color
        self.focused_border_color = focused_border_color
        self.border_width = border_width
        self.hover_border_width = hover_border_width
        self.click_border_width = click_border_width
        self.focused_border_width = focused_border_width
        self.font = font
        self.hover_font = hover_font
        self.click_font = click_font
        self.focused_font = focused_font
        self.text_color = text_color
        self.hover_text_color = hover_text_color
        self.click_text_color = click_text_color
        self.focused_text_color = focused_text_color
        self.text_size = text_size
        self.selection_text_color = selection_text_color
        self.selection_mark_color = selection_mark_color

        self.border_style = BorderStyle(self.border_color, self.border_width)
        self.hover_border_style = BorderStyle(self.hover_border_color, self.hover_border_width)
        self.click_border_style = BorderStyle(self.click_border_color, self.click_border_width)
        self.focused_border_style = BorderStyle(self.focused_border_color, self.focused_border_width)
