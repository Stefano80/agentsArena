import agentsArena
import unittest

class basicTest(unittest.TestCase):
    def test_createAgent(self):
        agent = agentsArena.createAgent()
        self.assertIsInstance(agent, agentsArena.Agent)
        self.assertEqual(agent.name, 'default')
        self.assertEqual(agent.elo(0), 0)
        self.assertEqual(agent.elo('bla'), 0)