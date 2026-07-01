import pyglet
from threading import Thread
from src.atomic import animateCalculation
from src.classes import batch, clock, windows

mainWindow = windows.mainWindow


# fpsLabel = pyglet.text.Label(f'FPS: {animateCalculation.fps}',
#     font_size=32,
#     x=16,y=16,
#     anchor_x='left', anchor_y='top',
#     color=(255,255,255),
#     batch=batch.batch
# )

fpsLabel = pyglet.window.FPSDisplay(mainWindow, (255,255,255))
    

@mainWindow.event
def on_draw():
    mainWindow.clear()

    # fpsLabel.text = f"FPS: {animateCalculation.fps}"
    batch.batch.draw()
    fpsLabel.draw()
    
    # print(animateCalculation.fps, animateCalculation.tickSpent, animateCalculation.deltaTime)



windows.InitWindowLocationAtom(mainWindow, True, (64,64))

def WindowMoveTest():
    clock.clock.sleep(5000000)
    windows.AnimateWindowLocation(window=mainWindow, locationFrom=(0,0), locationTo=(512,512), duration=5, ignoreLocationFix=True)

a = Thread(target=WindowMoveTest)
a.start()

pyglet.app.run()