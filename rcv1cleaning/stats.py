#!/usr/bin/env python
"""

"""
from __future__ import division
from collections import Counter

fname = '../data/targets-cleaned.csv'
# fname = '../data/test.csv'

with open(fname) as f:
    lines = f.read().splitlines()

numExamples = len(lines)

labelCounts = []
for line in lines:
    labelCounts.append(len(line.split(',')[1:]))

meanLabels = reduce(lambda x, y: x + y, labelCounts) / numExamples

print numExamples, 'examples'
print 'Average', meanLabels, 'labels per example'

counter = Counter()
splitLines = []
allLabels = []
labelSets = []

for line in lines:
    line = line.replace('"', '')
    parts = line.split(',')
    splitLines.append(parts)
    allLabels.extend(parts[1:])
    labelSets.append(', '.join(sorted(parts[1:])))
    for part in parts[1:]:
        counter[part] += 1

print 'most frequent labels:', Counter(allLabels).most_common(10)
print 'most frequent labels:', Counter(labelSets).most_common(10)