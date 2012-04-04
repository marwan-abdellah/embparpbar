#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A multiprocess `Pool` variant with a `ProgressBar`.

The `Pool` class from the multiprocessing is quite nice. What it lacks however,
is a progress bar. This module seeks to remedy that by providing a
ProgressPool.

Note: The progress bar used is available at:

    http://code.google.com/p/python-progressbar/


"""

__author__ = "Valentin Haenel <valentin.haenel@epfl.ch>"

import time
import random
from multiprocessing.pool import Pool
from progressbar import ProgressBar, Percentage, Bar, ETA 

class ProgressPool(Pool):
    """ Extension of `multiprocessing.Pool` with `ProgressBar`.

    The `map` function now displays a progress bar. The usual caveats about
    multiprocessing not working in an interactive interpreter apply.

    """

    def map(self, func, iterable, chunksize=1, pbar='ProgressPool'):
        """ Apply function on iterables in available subprocess workers.

        Parameters
        ----------
        func : callable
            the function to execute
        iterable : iterable
            the arguments to the func
        chunksize : int, default: 1
            the approximate number of tasks to distribute to a process at once
        pbar : str
            the string to display in the progress bar

        Returns
        -------
        results : list
            the result of applying func to each value in iterables

        """
        # need to get the length, for the progress bar
        if not hasattr(iterable, '__len__'):
            iterable = list(iterable)
        total_items = len(iterable)

        # initialize the progress bar
        pbar = ProgressBar(widgets=['%s: ' % pbar,
            Percentage(), Bar(), ETA()],
            maxval=total_items).start()

        # get the pool working asynchronously
        a_map = self.map_async(func, iterable, chunksize)

        # Crux: monitor the _number_left of the a_map, and update the progress
        # bar accordingly
        # TODO should probably check for termination on each run here
        while True:
            time.sleep(0.1)
            pbar.update(total_items-a_map._number_left)
            if a_map._number_left == 0:
                break
        pbar.finish()
        return a_map.get()

