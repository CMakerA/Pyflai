import abc
from Pyflai.dimensions import *


class UIElement(object):
    screen = None
    window = None

    def __init__(self, class_name: str, size: Size, position: Position):
        self.class_name = class_name
        self.id = None
        self.zone = Zone(position, position + size)
        self.size = size
        self.position = position

    on_element_tick = None

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def clear(self):
        pass
