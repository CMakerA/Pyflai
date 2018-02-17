from Pyflai.style.font.Font import *
from Pyflai.style.color import *

default = Font("monospace", color=Colors.white, size=15)

button_font = default.from_file(File(Directory("Pyflai/res/fonts"), "oswald.ttf"))
