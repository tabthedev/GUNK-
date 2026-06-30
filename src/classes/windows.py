# from src.classes import batch
from src.atomic import Atom
from src.classes import clock
from pyglet import window
from threading import Thread

mainWindow = window.Window(width=1920, height=1080, caption="GUNK!", resizable=False, style=window.Window.WINDOW_STYLE_DIALOG)

LocationFixedAtomByWindow: dict[window.BaseWindow, Atom[bool]] = {}
LocationAtomByWindow: dict[window.BaseWindow, Atom[tuple[int,int]]] = {}

def FixWindowLocation(window=mainWindow):
    locationFixedAtom = LocationFixedAtomByWindow[window]
    locationAtom = LocationAtomByWindow[window]

    while True:
        if not locationFixedAtom.get():
            pass
        p = locationAtom.get()
        window.set_location(p[0], p[1])

def InitWindowLocationAtom(window=mainWindow, initialActivated=False, initialLocation=(0,0)):
    activatedAtom = Atom(initialActivated)
    locationAtom = Atom(initialLocation)

    LocationFixedAtomByWindow[window] = activatedAtom
    LocationAtomByWindow[window] = locationAtom

    WLFixThread = Thread(target=FixWindowLocation, args=[window])
    WLFixThread.daemon = True
    WLFixThread.start()


def AnimateWindowLocation(window=mainWindow, locationFrom=(0,0), locationTo=(128,128), ignoreLocationFix=False):
    if not ignoreLocationFix and LocationFixedAtomByWindow[window].get():
        pass
    

# class CustomWindow:
#     def __init__(self, windowCaption="GUNK!", initSize=(1280,720), initPos=(0,0), initFullscreen=False, initResizable=False, initStyle=Window.WINDOW_STYLE_DIALOG):
#         self.window = Window(width=initSize[0], height=initSize[1], caption=windowCaption, fullscreen=initFullscreen, resizable=initResizable, style=initStyle)
#         self.window.set_location(x=initPos[0], y=initPos[1])
#         pass
    
#     def __getattr__(self, name):
#         return self._screen[name] or self._window[name]
    
#     def setPosition(self, pos:tuple[int, int]):
#         self.window.set_location(x=pos[0], y=pos[1])

#     def update(self):
#         self.window.clear()
#         batch.batch.draw()