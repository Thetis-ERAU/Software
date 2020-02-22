from threading import Timer
import time

class RepeatedTimer(object):
    '''from MestreLion @ StackOverflower'''
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval  # in ms
        self.function   = function
        self.args       = args      #function args
        self.kwargs     = kwargs    #function kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval/1000, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False