#!/usr/bin/env python
"""

"""
try:
    import cPickle as pickle
except:
    import pickle

from trainingproblem import TrainingProblem


fname = '../data/targets-cleaned-sorted.csv'
with open(fname) as f:
    lines = f.readlines()
targets = {}
for line in lines:
    line = line.replace('"', '')
    line = line.replace('\n', '')
    parts = line.split(',')
    targets[int(parts[0])] = parts[1:]


fname = '../data/lyrl2004_tokens_train.dat'
with open(fname) as f:
    lines = f.read().splitlines()

trainingProblems = []
trainingProblem = None
tokenLines = []
dId = None
for index, line in enumerate(lines):
    # print 'line:', line
    if line.startswith('.I'):
        if index > 1:
            trainingProblem.tokens = ' '.join(tokenLines)
            trainingProblem.targets = targets[dId]
            trainingProblems.append(trainingProblem)
        tokenLines = []
        dId = int(line.split(' ')[1])
        trainingProblem = TrainingProblem(dId)
    else:
        tokenLines.append(line)

trainingProblem.tokens = ' '.join(tokenLines)
trainingProblem.targets = targets[dId]
trainingProblems.append(trainingProblem)

print 'training problems:'
for problem in trainingProblems:
    print problem

outfile = open('../data/trainingproblems.p', 'w')
pickle.dump(trainingProblems, outfile)


outlist = []
for problem in trainingProblems:
    outlist.append(str(problem.did) + '\t' + ','.join(problem.targets) + '\t' + problem.tokens + '\n')

outfile = '../data/trainingproblems.csv'
with open(outfile, 'wb') as out:
    out.writelines(outlist)

