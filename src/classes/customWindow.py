from pyglet.window import Window
from pyglet.graphics import Batch

batch = Batch()

class CustomWindow:
    def __init__(self, windowCaption="GUNK!", initSize=(1280,720), initPos=(0,0), initFullscreen=False, initBorderless=True, initResizable=False):
        self.window = Window(width=initSize[0], height=initSize[1], caption=windowCaption, fullscreen=initFullscreen, resizable=initResizable, style=initBorderless and Window.WINDOW_STYLE_DIALOG or Window.WINDOW_STYLE_OVERLAY)
        self.window.set_location(x=initPos[0], y=initPos[1])
        pass
    
    def __getattr__(self, name):
        return self._screen[name] or self._window[name]
    
    def setPosition(self, pos:tuple[int, int]):
        self.window.set_location(x=pos[0], y=pos[1])

    def update(self):
        self.window.clear()
        batch.draw()