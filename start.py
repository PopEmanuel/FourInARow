from ui.console import console
from ui.gui import gui

ui = 'gui'

if ui == 'gui':
    start = gui()
else:
    start = console()

start.start()