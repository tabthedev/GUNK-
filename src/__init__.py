import pyglet
from src.classes import customWindow

window = customWindow.CustomWindow(initPos=(500,500))
batch = customWindow.batch

@window.window.event
def on_draw():
    window.update()

pyglet.app.run()