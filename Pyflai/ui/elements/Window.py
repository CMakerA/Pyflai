from Pyflai.dimensions import *
from Pyflai.style.color import *
from Pyflai.ui.UIElement import *
import pygame
from Pyflai.system.ui.Ider import *


class Window:
    running = True

    """This is called when starting the main loop. Before initializing the ui"""
    on_start_bu = None
    """This is called when starting the main loop. After initializing the ui"""
    on_start_au = None
    """This is called when stopping the main loop. Before stopping the ui"""
    on_end_bu = None
    """This is called when stopping the main loop. After stopping the ui"""
    on_end_au = None
    """This is called before drawing all the elements"""
    on_start_tick = None
    """This is called every time before drawing each element."""
    on_element_tick = None
    """This is called every update, when searching for the events"""
    on_event = None
    """This is called when finished drawing all elements"""
    on_tick = None

    def __init__(self, size: Size = None, background_color: Color.NoAlpha = Color(0, 0, 0), title: str = "",
                 fullscreen: bool = False):
        if size is not None:
            self.size = size
            self.fullscreen = fullscreen
        else:
            self.size = None
            self.fullscreen = True
        self.title = title
        self.elements = []
        self.screen = None
        self.background_color = background_color
        self.ider = Ider(["ImageView", "Label", "Button"])

    def add(self, element: UIElement):
        self.ider.set(element)
        self.elements.append(element)

    lastElementReadIndex = 0

    lastEventReadIndex = 0

    def mouse_position(self) -> Vector2:
        mouse_get_pos = pygame.mouse.get_pos()
        mouse_x = mouse_get_pos[0]
        mouse_y = mouse_get_pos[1]
        mouse_pos = Vector2(mouse_x, mouse_y)
        return mouse_pos

    def start(self):
        if self.on_start_bu:
            self.on_start_bu()

        pygame.init()

        self.screen = pygame.display.set_mode(self.size.get() if self.size is not None else (
            pygame.display.Info().current_w, pygame.display.Info().current_h),
                                              pygame.FULLSCREEN if self.fullscreen else pygame.RESIZABLE)

        for element in self.elements:
            element.screen = self.screen
            element.window = self

        if self.title is not None and self.title is not "":
            pygame.display.set_caption(self.title)

        self.screen.fill(self.background_color.get())

        if self.on_start_au:
            self.on_start_au()

        while self.running:
            if self.on_start_tick is not None:
                self.on_start_tick()

            if len(self.elements) > 0:
                if self.lastElementReadIndex > len(self.elements) - 1:
                    self.lastElementReadIndex = 0
                self.elements[self.lastElementReadIndex].clear()
                self.elements[self.lastElementReadIndex].draw()
                if self.elements[self.lastElementReadIndex].on_element_tick is not None:
                    self.elements[self.lastElementReadIndex].on_element_tick(self.elements[self.lastElementReadIndex])
                if self.on_element_tick is not None:
                    self.on_element_tick(self.elements[self.lastElementReadIndex])
                self.lastElementReadIndex += 1

            if self.on_tick is not None:
                self.on_tick()

            for event in pygame.event.get():
                if self.on_event is not None:
                    self.on_event(event)
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                self.lastEventReadIndex += 1

            pygame.display.flip()
        if self.on_end_bu:
            self.on_end_bu()
        pygame.quit()
        if self.on_end_au:
            self.on_end_au()
