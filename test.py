from Pyflai.ui.elements import *
from Pyflai.style.color import *
from Pyflai.dimensions import *

# on_element_tick must not be used by user!

window = Window(size=Size(1000, 800), background_color=Colors.flat_frosted_ice.no_alpha(), title="Title")

label = Label(position=Position(10, 10), text="Mouse").with_font_color(Colors.red).with_font_size(50)


def label_tick(self):
    self.position = window.mouse_position()
    print("new " + self.id + " position is " + self.position.to_string())


# label.on_element_tick = label_tick

window.add(label)

window.start()
