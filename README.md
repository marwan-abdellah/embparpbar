# embparpbar

Embarrassingly Parallel with a Progress Bar

## Description

The ``Pool`` class from the multiprocessing is quite nice. What it lacks
however, is a progress bar. This module seeks to remedy that by providing a
ProgressPool.

The progress bar is from: http://code.google.com/p/python-progressbar/

## Installation

Everything is in the file ``embparpbar.py`` , so just drop that file to where
you want to use it.

## Usage

See the
[example.py](https://github.com/esc/embparpbar/blob/d94cd5c801aae9d1e41db4942ad2a681bebe4da2/example.py).
for details.

It will look like::

    zsh» ./example.py
    Using a normal Pool... you never know when it is done...
    Oh... finally... it has completed...


    Now using a ProgressPool... enjoy the ride! :D
    ProgressPool: 100%|###############################################|Time: 00:00:20

    Now using a ProgressPool, with a custom progressbar! :D
    Come on baby, let's do the twist:  ||| Time: 00:00:22


## Website

Repository is at: https://github.com/esc/embparpbar

## Author, Copyright and License

(C) 2012 Valentin Haenel <valentin.haenel@epfl.ch>

embparpbar is licensed under the terms of the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FR
