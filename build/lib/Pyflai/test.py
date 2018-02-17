from ui.elements import *
from style.color import *
from dimensions import *
from style.font import *

window = Window(background_color=Color.from_hex("#2d3436").no_alpha(), title="Title")

button = Button(Position(10, 10), Size(150, 50), "Button")

window.add(button)

window.start()
