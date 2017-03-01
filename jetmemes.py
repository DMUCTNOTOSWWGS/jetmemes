#!/usr/bin/env python3

import itertools
from random import shuffle

l = ['jet','fuel','melt','steel','beams']
perm = list(itertools.permutations(l))
shuffle(perm)
for a in perm:
    print("{} {} can't {} {} {}".format(a[0],a[1],a[2],a[3],a[4]))
