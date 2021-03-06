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
    print "Using a normal Pool... you never know when it is done..."
    pool = Pool()
    pool.map(f, range(100))
    print "Oh... finally... it has completed...\n"
    print ""
    time.sleep(3)

    print "Now using a ProgressPool... enjoy the ride! :D"
    ppool = ProgressPool()
    ppool.map(f, range(100))
    print ""
    time.sleep(3)

    print "Now using a ProgressPool, with a custom progressbar! :D"
    pbar = ProgressBar(widgets=['%s: ' % "Come on baby, let's do the twist",
        ' ', RotatingMarker(), RotatingMarker(), RotatingMarker(), ' ', ETA()],
        maxval=100).start()
    ppool.map(f, range(100), pbar=pbar)
