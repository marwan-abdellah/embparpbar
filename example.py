#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An example of using the `ProgressPool`

@author  Valentin Haenel <valentin.haenel@epfl.ch>

"""

import time
import random
from progresspool import ProgressPool

def f(x):
    time.sleep(random.uniform(0,3))
    return x*x

if __name__ == '__main__':
    pp = ProgressPool()
    print pp.map(f, range(100))
