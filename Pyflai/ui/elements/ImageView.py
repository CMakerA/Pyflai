from Pyflai.drawing import *
from Pyflai.dimensions import *
from Pyflai.ui.UIElement import *


class ImageView(UIElement):
    def __init__(self, image: Image, size: Size, position: Position):
        super().__init__("ImageView", size, position)
        self.image = image
        self.image_rect = self.zone

    def draw(self):
        if self.screen is not None:
            self.screen.blit(self.image.instance, self.image_rect)

    def clear(self):
        if self.screen is not None:
            Helper.draw_rect(self.zone, self.window.background_color, self.screen)
