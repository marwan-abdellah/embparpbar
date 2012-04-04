#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An example of using the `ProgressPool`

@author  Valentin Haenel <valentin.haenel@epfl.ch>

"""

import time
import random
from multiprocess import Pool
from progresspool import ProgressPool

def f(x):
    time.sleep(random.uniform(0,3))
    return x*x

if __name__ == '__main__':
    # using a normal pool
    p = Pool()
    print p.map(f, range(100))

    # using a ProgressPool
    pp = ProgressPool()
    print pp.map(f, range(100))
