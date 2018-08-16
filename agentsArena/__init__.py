def createAgent():
    return Agent()

def createMatch():
    return Match()


class Agent:
    def __init__(self):
        self.name = 'default'
        self.bayesElo  = lambda x: 0

class Match:
    def __init__(self):
        self.agents = []

    def addAgent(self, agent):
        self.agents.append(agent)

    def eloDifference(self):
        return self.agents[0].bayesElo(0) - self.agents[1].bayesElo(0)