#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An example of using the `ProgressPool`. """

__author__ = "Valentin Haenel <valentin.haenel@epfl.ch>"

import time
import random
from multiprocessing import Pool
from embparpbar import ProgressPool
from progressbar import ProgressBar, RotatingMarker, ETA

def f(x):
    time.sleep(random.uniform(0, 3))
    return x*x

if __name__ == '__main__':
    print "Using a normal pool... you never know when it is done..."
    pool = Pool()
    pool.map(f, range(100))
    print "Oh... finally... it has completed...\n"

    time.sleep(3)

    print "Now using a progress pool... enjoy the ride! :D"
    ppool = ProgressPool()
    ppool.map(f, range(100))

    print "Now using a progress pool, with a custom progressbar... enjoy the ride! :D"
    pbar = ProgressBar(widgets=['%s: ' % "Come on baby, lets do the twist",
        ' ', RotatingMarker(), RotatingMarker(), RotatingMarker(), ' ', ETA()],
        maxval=100).start()
    ppool.map(f, range(100), pbar=pbar)
