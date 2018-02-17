from Pyflai.ui import *
from Pyflai.dimensions import *


class Ider:
    def __init__(self, element_types: []):
        self.element_types = element_types
        self.ids = dict({str("Initializer"): UIElement("None", Size(0, 0), Position(0, 0))})

    def set(self, element: UIElement):
        if element.class_name in self.element_types:
            element_id = self.__get_available_id(element)
            self.ids[element_id] = element
            element.id = element_id

    __counter = 0

    def __get_available_id(self, element) -> str:
        self.__counter = 0
        return self.__get_available_id_iterator(element)

    def __get_available_id_iterator(self, element) -> str:
        try:
            element_id = self.ids[element.class_name + str(self.__counter)]
            self.__counter += 1
            self.__get_available_id_iterator(element)
        except KeyError:
            return element.class_name + str(self.__counter)
