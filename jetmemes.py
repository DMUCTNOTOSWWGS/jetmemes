#!/usr/bin/env python3

import itertools

l = ['jet','fuel','melt','steel','beams']
for a in itertools.permutations(l):
    print("{} {} can't {} {} {}".format(a[0],a[1],a[2],a[3],a[4]))

