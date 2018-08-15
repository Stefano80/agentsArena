def createAgent():
    return Agent()

def createMatch():
    return Match()


class Agent:
    def __init__(self):
        self.name = 'default'
        self.elo  = lambda x: 0

class Match:
    def __init__(self):
        self.agents = []