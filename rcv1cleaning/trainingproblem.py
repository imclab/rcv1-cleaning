"""

"""


class TrainingProblem(object):

    def __init__(self, did):
        self.did = did
        self.tokens = None
        self.targets = []

    def __str__(self):
        return 'DID: %s\n%s\n%s' % (self.did, self.tokens, self.targets)