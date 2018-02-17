from Pyflai.style.style.Style import *
from Pyflai.style.font import *

no_style = SingleStyle(Colors.transparent, BorderStyle(Colors.transparent, 0), Fonts.default, Colors.transparent)

button_idle = SingleStyle(Colors.flat_gray, BorderStyle(Colors.transparent, 1), Fonts.default, Colors.transparent,
                          "ButtonIdle")
button_hovered = button_idle.clone().with_background_color(Colors.flat_island_green).with_name("ButtonHovered")
button_clicked = button_hovered.clone().with_name("ButtonClicked")
button_right_clicked = button_hovered.clone().with_name("ButtonRightClicked")

button = Style(button_idle, button_clicked, button_right_clicked, button_hovered, no_style)

text_box_idle = SingleStyle(Colors.white, BorderStyle(Colors.black, 1), Fonts.default, Colors.flat_gray)
text_box_hovered = text_box_idle
text_box_clicked = text_box_idle
text_box_right_clicked = text_box_idle
text_box_focused = SingleStyle(Colors.flat_cream_yellow, BorderStyle(Colors.flat_blue, 2), Fonts.default,
                               Colors.flat_gray)

text_box = Style(text_box_idle, text_box_clicked, text_box_right_clicked, text_box_hovered, text_box_focused)
