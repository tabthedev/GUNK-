import pyglet
from threading import Thread
from src.atomic.Atom import Atom
from src.classes import batch, clock, windows

mainWindow = windows.mainWindow

@mainWindow.event
def on_draw():
    mainWindow.clear()
    batch.batch.draw()
        
windows.InitWindowLocationAtom(mainWindow, True, (500,32))

pyglet.app.run()