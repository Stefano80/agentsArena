import agentsArena
import unittest

class basicTest(unittest.TestCase):
    def test_createAgent(self):
        agent = agentsArena.createAgent()
        self.assertIsInstance(agent, agentsArena.Agent)
        self.assertEqual(agent.name, 'default')