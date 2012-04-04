import time
import random
from multiprocessing.pool import Pool
from progressbar import ProgressBar, Percentage, Bar, ETA 

def f(x):
    time.sleep(random.uniform(0,3))
    return x*x

class ProgressPool(Pool):

    def map(self, func, iterable, chunksize=1, pbar='ProgressPool'):

        # need to get the length, for the progressbar
        if not hasattr(iterable, '__len__'):
            iterable = list(iterable)
        total_items = len(iterable)

        # initialize the progress bar
        pbar = ProgressBar(widgets=['%s: ' % pbar,
            Percentage(), Bar(), ETA()],
            maxval=total_items).start()

        # get the pool working aysnchronously
        a_map = self.map_async(func, iterable, chunksize)

        # Crux: monitor the _number_left of the a_map, and update the progressbar
        # accordingly
        # TODO should probably check for termination on each run here
        while True:
            time.sleep(0.1)
            pbar.update(total_items-a_map._number_left)
            if a_map._number_left == 0:
                break
        pbar.finish()
        return a_map.get()

if __name__ == '__main__':
    pp = ProgressPool()
    print pp.map(f, range(100))
