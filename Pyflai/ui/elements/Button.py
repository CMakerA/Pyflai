from Pyflai.drawing import *
from Pyflai.dimensions import *
from Pyflai.ui.UIElement import *
from Pyflai.style.font import *
from Pyflai.ui.elements.Label import *
import pygame
from Pyflai.drawing import *
from Pyflai.style.style import *
from Pyflai.style.color import *


class Button(UIElement):
    # TODO: Change style depending on status: Idle, Click, Hover

    on_right_click = None
    on_click = None
    on_hover = None
    on_leave = None

    def __init__(self, position: Position, size: Size, text: str, styles: Style = Styles.button):
        super().__init__("Button", size, position)
        pygame.font.init()
        self.text = text
        self.styles = styles
        self.current_style = self.styles.idle_style
        # TODO: Generate label
        self.on_element_tick = self.__tick
        self.label = None

    # <editor-fold desc="with_* methods">
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
    # </editor-fold>

    # <editor-fold desc="Drawing methods">
    def update(self):
        self.label = Label(self.position, self.text, self.current_style.font)

    def draw(self):
        Helper.draw_rect(self.zone, self.current_style.background_color, self.screen)
        if self.label is not None:
            self.label.draw()

    def clear(self):
        if self.screen is not None:
            Helper.draw_rect(self.zone, self.window.background_color, self.screen)
    # </editor-fold>

    just_hovered = False
    just_clicked = False
    just_right_clicked = False
    just_left = False

    hovered = False
    clicked = False
    right_clicked = False
    left = False

    def __tick(self):
        mouse_get_pos = pygame.mouse.get_pos()
        mouse_x = mouse_get_pos[0]
        mouse_y = mouse_get_pos[1]
        mouse_pos = Vector2(mouse_x, mouse_y)
        if self.zone.point_over(mouse_pos):
            self.hovered = True
            self.left = False
            self.just_clicked = False
            if not self.just_hovered and self.on_hover is not None:
                self.just_hovered = True
                self.on_hover()
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                if not self.just_clicked and self.on_click is not None:
                    self.just_clicked = True
                    self.on_click()
            else:
                self.clicked = False
                self.just_clicked = False
            if pygame.mouse.get_pressed()[1]:
                self.right_clicked = True
                if not self.just_right_clicked and self.on_right_click is not None:
                    self.just_right_clicked = True
                    self.on_right_click()
            else:
                self.right_clicked = False
                self.just_right_clicked = False
        else:
            self.hovered = False
            self.left = True
            self.just_hovered = False
            self.just_clicked = False
            self.just_right_clicked = False
            if not self.just_left and self.on_leave is not None:
                self.just_left = True
                self.on_leave()
        self.__update_styles()

    def __update_styles(self):
        if self.clicked:
            print("Clicked " + self.id)
            self.current_style = self.styles.clicked_style
        elif self.right_clicked:
            print("Right Clicked " + self.id)
            self.current_style = self.styles.right_clicked_style
        elif self.hovered:
            print("Hovered " + self.id)
            self.current_style = self.styles.hovered_style
        else:
            self.current_style = self.styles.idle_style
            print("Left " + self.id)
        print("Background Color is " + self.current_style.background_color.to_string() + ". Current style is " + self.current_style.name)
