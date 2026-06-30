# from src.classes import batch
from pyglet import window

mainWindow = window.Window(width=1920, height=1080, caption="GUNK!", resizable=False, style=window.Window.WINDOW_STYLE_DIALOG)

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