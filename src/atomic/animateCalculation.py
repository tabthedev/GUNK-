from threading import Thread
from src.classes import clock

deltaTime = 0
tickrate = 120

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
    global deltaTime, tickSpent, fps
    deltaTime = clock.clock.update_time()
    tickSpent += 1
    fps += 1
    
    clock.clock.sleep(1000000/tickrate)

animThread = Thread(target=TickCalculation)
animThread.daemon = True
animThread.start()