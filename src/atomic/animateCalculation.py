from threading import Thread
from src.classes import clock

deltaTime = 0
tickrate = 60

def TickCalculation():
    global deltaTime
    deltaTime = clock.clock.update_time()
    clock.clock.sleep(1/tickrate)


animThread = Thread(target=TickCalculation)
animThread.daemon = True
animThread.start()