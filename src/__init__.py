import pyglet
from src.atomic import animateCalculation
from src.classes import batch, windows

mainWindow = windows.mainWindow

@mainWindow.event
def on_draw():
    mainWindow.clear()

    fpsLabel = pyglet.text.Label(f'FPS: {animateCalculation.fps}',
        font_size=32,
        x=16,y=16,
        anchor_x='left', anchor_y='top'
                                 )
    fpsLabel.text

    batch.batch.draw()
        
windows.InitWindowLocationAtom(mainWindow, True, (500,32))

pyglet.app.run()