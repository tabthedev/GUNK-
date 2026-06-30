import pyglet
from threading import Thread
from src.atomic.Atom import Atom
from src.classes import batch, clock, windows

mainWindow = windows.mainWindow

@mainWindow.event
def on_draw():
    mainWindow.clear()
    batch.batch.draw()
        

mainWindowLocationAtom = Atom((0,32))

mainWindowFixThread = Thread(target=windows.FixWindowLocation, kwargs={'locationAtom':mainWindowLocationAtom})
mainWindowFixThread.daemon = True
mainWindowFixThread.start()

pyglet.app.run()


mainWindow.set_location