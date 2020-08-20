import threading


class _background_work:
    def __init__(self, concurrency=8):
        self.sem = threading.Semaphore(concurrency)

    def _runner(self, function, *args, **kwargs):
        try:
            # can we get a future out of this?
            function(*args, **kwargs)
        finally:
            self.sem.release()

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            self.sem.acquire()
            threading.Thread(
                target=self._runner,
                args=(function, *args),
                kwargs=kwargs,
            ).start()
        return wrapper


'''
usage:
    @background_work(concurrency=5)
    def my_fun(foo, bar=bar)
        pass
'''
def background_work(function=None, **kwargs):
    if function and callable(function):
        return _background_work()(function)
    else:
        return _background_work(**kwargs)
