def createAgent():
    return Agent()


class Agent:
    def __init__(self):
        self.name = 'default'
        self.elo  = lambda x: 0