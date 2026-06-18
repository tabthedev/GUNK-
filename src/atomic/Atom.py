import threading

class Atom:
    def __init__(self, initial):
        self._value = initial
        self._lock = threading.Lock()

    def set(self, value):
        with self._lock:
            self._value = value
            return self._value

    def get(self):
        with self._lock:
            return self._value
