from pygame import display, window

display.init()

class CustomWindow:
    def __init__(self, windowName="GUNK!", initSize=(1280,720), initPos=(0,0), initFullscreen=False, initBorderless=True, initResizable=False, alwaysOnTop=False):
        self._screen = display.set_mode(initSize)
        self._window = window.Window(windowName, initSize, initPos, fullscreen=initFullscreen, opengl=True, borderless=initBorderless, resizable=initResizable, allow_high_dpi=True, always_on_top=alwaysOnTop)
        pass
    
    def __getattr__(self, name):
        return self._screen[name] or self._window[name]
    
    def setPosition(self, pos:tuple[int, int]):
        display.set_window_position(pos)

    def update(self):
        self._window.flip()
        