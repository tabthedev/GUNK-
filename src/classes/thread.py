from threading import Thread as Thread_P

aliveThreads = []

class Thread(Thread_P):
    def __init__(self, target, kwargs):
        super().__init__(target=target, kwargs=kwargs, daemon=True)
        aliveThreads.append(self)

    def kill(self):
        aliveThreads.remove(self)
