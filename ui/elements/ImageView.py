from drawing import *
from dimensions import *
from ui.UIElement import *


class ImageView(UIElement):
    def __init__(self, image: Image, size: Size, position: Position):
        super().__init__("ImageView", size, position)
        self.image = image
        self.image_rect = self.zone

    def draw(self):
        if self.screen is not None:
            self.screen.blit(self.image.instance, self.image_rect)
