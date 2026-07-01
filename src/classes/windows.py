# from src.classes import batch
from src.atomic import Atom, animateCalculation
from pyglet import window
from threading import Thread
from math import floor

mainWindow = window.Window(width=512, height=512, caption="GUNK!", resizable=False, style=window.Window.WINDOW_STYLE_DIALOG)

LocationFixedAtomByWindow = {}
LocationAtomByWindow = {}

def FixWindowLocation(window=mainWindow):
    locationFixedAtom = LocationFixedAtomByWindow[window]
    locationAtom = LocationAtomByWindow[window]

    while True:
        if not locationFixedAtom.get():
            continue
        p = locationAtom.get()
        window.set_location(p[0], p[1])
        animateCalculation.WaitTicks()

def InitWindowLocationAtom(window=mainWindow, initialActivated=False, initialLocation=(0,0)):
    activatedAtom = Atom.Atom(initialActivated)
    locationAtom = Atom.Atom(initialLocation)

    LocationFixedAtomByWindow[window] = activatedAtom
    LocationAtomByWindow[window] = locationAtom

    WLFixThread = Thread(target=FixWindowLocation, args=[window])
    WLFixThread.daemon = True
    WLFixThread.start()


def AnimateWindowLocation(window=mainWindow, locationFrom=(0,0), locationTo=(128,128), duration=1, ignoreLocationFix=False):
    locationFixedAtom = LocationFixedAtomByWindow[window]
    locationAtom = LocationAtomByWindow[window]
    
    if not locationFixedAtom or not locationAtom:
        pass

    if not ignoreLocationFix and locationFixedAtom.get():
        pass
    
    xFrom,yFrom,xTo,yTo = locationFrom[0], locationFrom[1], locationTo[0], locationTo[1]

    timeSpent = 0
    while timeSpent < duration:
        timeSpent += animateCalculation.WaitTicks()
        if timeSpent > duration:
            timeSpent = duration
        locationAtom.set(
            (
                floor(xFrom + timeSpent/duration * (xTo - xFrom)),
                floor(yFrom + timeSpent/duration * (yTo - yFrom))
            )
        )

    



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