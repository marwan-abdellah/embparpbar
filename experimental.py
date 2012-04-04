import multiprocessing
from multiprocessing import Pool
from progressbar import ProgressBar, Percentage, Bar, ETA 
import time

multiprocessing.log_to_stderr()

def f(x):
    time.sleep(1)
    return x*x

class LazyProgressBar(ProgressBar):

    def __init__(self, *args, **kwargs):
        self.counter = 0
        super(LazyProgressBar,self).__init__(*args, **kwargs)

    def update(self, arg):
        if arg is not None:
            super(LazyProgressBar,self).update(arg)
        else:
            super(LazyProgressBar,self).update(self.counter)
            self.counter += 1

class Updater(object):

    def __init__(self, func, pbar):
        self.func = func
        self.pbar = pbar

    def __call__(self, args):
        result = self.func(args[0])
        self.update(args[1])
        return result

    def update(self, arg):
        pass
        #self.pbar.update(arg)

class ProgressPool():

    def __init__(self, processes=None, pbar_text="ProgressPool"):
        self.pool = Pool(processes=processes)
        self.pbar_text = pbar_text
        self.pbar = None

    def map_async(self, func, iterable, chunksize=None, callback=None):
        # create the progressbar
        self.pbar = ProgressBar(widgets=['%s: ' % self.pbar_text,
            Percentage(), Bar(), ETA()],
            maxval=len(iterable)).start()
        # create the updater
        updater = Updater(func, self.pbar)
        enumerated = [(i,j) for i,j in enumerate(iterable)]
        return self.pool.map_async(updater, enumerated, chunksize,
                callback)

    def finish(self):
        self.pbar.finish()

if __name__ == '__main__':
    pool = Pool(4)
    print pool._pool
    amap = pool.map_async(f, range(100), 1)
    pbar = ProgressBar(widgets=['%s: ' % 'Testing',
        Percentage(), Bar(), ETA()],
        maxval=100).start()
    while True:
        time.sleep(0.1)
        #print len(pool._cache)
        pbar.update(100-amap._number_left)
        if amap._number_left == 0:
            break
    pbar.finish()
    #result = amap.get()
    #print result
    #print result
    #while True:
    #    amap.wait(timeout=1)
    #    print amap._number_left
    #    if amap.ready():
    #        break
    #print amap._number_left
    #pool.finish()

