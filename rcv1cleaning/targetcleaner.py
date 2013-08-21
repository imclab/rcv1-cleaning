#!/usr/bin/env python
"""


"""

fname = '../data/rcv1-v2.topics.qrels'
with open(fname) as f:
    lines = f.readlines()

targets = {}

print 'Reading list'
counter = 0
for line in lines:
    counter += 1
    if counter % 500 == 0:
        print counter
    parts = line.split(' ')
    key = parts[1]
    value = parts[0]
    if targets.has_key(key):
        targets[key].append(value)
    else:
        targets[key] = [value]

print 'Processing list'
outlist = []
counter = 0
for target in targets:
    counter += 1
    if counter % 500 == 0:
        print counter
    outlist.append(target + ',"' + ','.join(targets[target]) + '"\n')

print 'Writing list'
outfile = '../data/targets-cleaned.csv'
with open(outfile, 'wb') as out:
    out.writelines(outlist)


print 'target 2289:', targets[2289]