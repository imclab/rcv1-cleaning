#!/usr/bin/env python
"""

"""

fname = '../data/rcv1-v2.topics.qrels'
with open(fname) as f:
    lines = f.readlines()

numLines = len(lines)
startIndex = 0
endIndex = 200000

counter = 0
while endIndex < numLines:
    outfile = '../data/out' + str(counter)
    with open(outfile, 'wb') as out:
        out.writelines(lines[startIndex:endIndex])
    startIndex += 200000
    endIndex += 200000
    counter += 1


outfile = '../data/out' + str(counter)
with open(outfile, 'wb') as out:
    out.writelines(lines[startIndex:])
