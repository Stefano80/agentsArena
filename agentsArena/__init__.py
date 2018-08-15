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

    def addAgent(self, agent):
        self.agents.append(agent)

    def eloDifference(self):
        return self.agents[0].elo(0) - self.agents[1].elo(0)