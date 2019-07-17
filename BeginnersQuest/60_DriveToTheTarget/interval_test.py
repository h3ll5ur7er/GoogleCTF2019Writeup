from time import sleep
from threading import Thread, Event
from functools import wraps

def set_interval(interval):
    def decorator(function):
        @wraps(function)
        def wrapper(*a, **kw):
            stopped = Event()

            def loop():
                while not stopped.wait(interval):
                    function(*a, **kw)

            t = Thread(target=loop)
            t.daemon = True
            t.start()
            return stopped
        return wrapper
    return decorator
"""
class Foo:
    @set_interval(1)
    def tst(self):
        print("tick")
t = Foo()
stop = t.tst()
sleep(10)
stop.set()

"""

@set_interval(1)
def tst():
    print("tick")
    
stop = tst()
sleep(10)
stop.set()