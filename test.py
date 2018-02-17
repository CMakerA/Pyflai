from Pyflai.ui.elements import *
from Pyflai.style.color import *
from Pyflai.dimensions import *
from Pyflai.style.font import *
from Pyflai.system.filesystem import *

# on_element_tick must not be used by user!

window = Window(size=Size(1000, 800), background_color=Colors.flat_frosted_ice.no_alpha(), title="Title")

button = Button(Position(10, 10), Size(150, 50), "Button")

window.add(button)

window.start()
