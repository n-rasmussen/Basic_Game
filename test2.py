import time as time


class Stopwatch():
    def __int__(self, start):
        self._start = start

    def get_seconds(self):
        return int(time.time() - self._start)


clock = Stopwatch()
clock._start = time.time()
print(clock._start)
time.sleep(3)
print(clock.get_seconds())
clock._start = time.time()
print(clock.get_seconds())