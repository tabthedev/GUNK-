from threading import Thread
from src.classes import clock, windows

deltaTime = 0
tickrate = 144

tickSpent = 0

fps = 0

def FPSdecrement():
    clock.clock.sleep(1000000)
    global fps
    fps -= 1

def WaitTicks(tick=1):
    # curTick = tickSpent
    # while curTick+tick > tickSpent:
    #     continue
    dtS = 0
    for i in range(tick):
        dtS += clock.clock.tick()

    return dtS



def TickCalculation():
    while True:
        global deltaTime, tickSpent, fps
        deltaTime = 0
        while deltaTime < 1/tickrate:
            deltaTime += WaitTicks()
        tickSpent += 1
        fps += 1

        fpsDecrementThr = Thread(target=FPSdecrement)
        fpsDecrementThr.daemon = True
        fpsDecrementThr.start()


animThread = Thread(target=TickCalculation)
animThread.daemon = True
animThread.start()