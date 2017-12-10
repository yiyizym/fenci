#!/usr/local/bin/python
# -*- coding: utf-8 -*-
def numeric_compare(x, y):
    result = float(x.split(':')[1]) - float(y.split(':')[1])
    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0
with open('b_c.txt', 'r+') as f:
    raw = f.readlines()
    raw_sorted = sorted(raw, cmp=numeric_compare)
    f.seek(0)
    f.writelines(raw_sorted)
    f.truncate()
    print 'finished'