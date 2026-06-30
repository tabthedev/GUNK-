from threading import Thread
from src.classes import clock

deltaTime = 0
tickrate = 60

tickSpent = 0

def WaitTicks(tick=1):
    # clock.clock.sleep(1/tickrate*tick)
    curTick = tickSpent
    while curTick+tick > tickSpent:
        continue

def TickCalculation():
    global deltaTime, tickSpent
    deltaTime = clock.clock.update_time()
    tickSpent += 1
    WaitTicks()

animThread = Thread(target=TickCalculation)
animThread.daemon = True
animThread.start()