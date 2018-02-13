from system.filesystem import *
import pygame


class Image:
    def __init__(self, file: File):
        self.file = file
        self.instance = pygame.image.load(self.file.path)

    def __is_image(self) -> bool:
        return self.file.extension is "png"\
               or self.file.extension is "jpg"\
               or self.file.extension is "jpeg"\
               or self.file.extension is "gif"\
               or self.file.extension is "svg"
