#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import time

def slop(df):
    pass

def _time_analyze_(func):
    t1_start = time.perf_counter()
    func()
    t1_stop = time.perf_counter()
    print(func.__name__)
    print("Elapsed time: %s s" % (t1_stop - t1_start))


if __name__ == '__main__':
    _time_analyze_(main)
