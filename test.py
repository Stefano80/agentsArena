import agentsArena
import unittest

class basicTest(unittest.TestCase):
    def test_createAgent(self):
        agent = agentsArena.createAgent()
        self.assertIsInstance(agent, agentsArena.Agent)
        self.assertEqual(agent.name, 'default')
        self.assertEqual(agent.elo(0), 0)
        self.assertEqual(agent.elo('bla'), 0)
        self.assertEqual(agent.elo(range(1000)), 0)

    def test_modifyAgent(self): 
        agent = agentsArena.createAgent()
        agent.elo = lambda x: x**2
        agent.name = 'new agent'
        self.assertEqual(agent.elo(2), 4)
        self.assertEqual(agent.name, 'new agent')

    def test_createMatch(self):
        match = agentsArena.createMatch()
        match.addAgent(agentsArena.createAgent())
        match.addAgent(agentsArena.createAgent())
        self.assertEqual(match.eloDifference(), 0)
        