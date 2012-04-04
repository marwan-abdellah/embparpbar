from multiprocessing import Process, Queue
import time
import random
from progressbar import ProgressBar, Percentage, Bar, ETA 

def f(id_, queue):
    time.sleep(random.uniform(0,1))
    queue.put(id_)

class ProgressPool(object):

    def __init__(self, processes):
        self.processes = processes
        self.slots = []

    def map(self, func, sequence):
        q = Queue()
        total = 0
        pbar = ProgressBar(widgets=['%s: ' % 'Testing',
            Percentage(), Bar(), ETA()],
            maxval=len(sequence)).start()
        while True:
            while len(self.slots) < self.processes and len(sequence) != 0:
                # free slots available, allocate them
                p = Process(target=f, args=(sequence.pop(), q))
                p.start()
                self.slots.append(p)
            q.get()
            total+=1
            pbar.update(total)
            for p in self.slots:
                # check if anything completed
                if not p.is_alive():
                    self.slots.remove(p)
                    break
            if len(sequence) == 0:
                break
        pbar.finish()

if __name__ == '__main__':
    pp = ProgressPool(4)
    pp.map(f, range(100))
