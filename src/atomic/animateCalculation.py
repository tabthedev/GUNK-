from threading import Thread
from src.classes import clock

deltaTime = 0
tickrate = 60

def WaitTicks(tick=1):
    clock.clock.sleep(1/tickrate*tick)

def TickCalculation():
    global deltaTime
    deltaTime = clock.clock.update_time()
    WaitTicks()

animThread = Thread(target=TickCalculation)
animThread.daemon = True
animThread.start()