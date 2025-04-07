import unittest
from unittest.mock import patch
import random
from enum import Enum

# Assuming the code you provided is in a file named 'main.py'
# If it's in a different file, adjust the import accordingly
from main import Action, Strategy, AlwaysCooperateStrategy, RandomStrategy


class TestAction(unittest.TestCase):
    def test_action_enum(self):
        self.assertEqual(Action.COOPERATE.value, 1)
        self.assertEqual(Action.DEFECT.value, 2)


class TestStrategy(unittest.TestCase):
    def test_strategy_initialization(self):
        strategy = Strategy("Test Strategy")
        self.assertEqual(strategy.name, "Test Strategy")

    def test_strategy_execute_not_implemented(self):
        strategy = Strategy("Test Strategy")
        with self.assertRaises(NotImplementedError):
            strategy.execute()


class TestAlwaysCooperateStrategy(unittest.TestCase):
    def test_always_cooperate_strategy_initialization(self):
        strategy = AlwaysCooperateStrategy()
        self.assertEqual(strategy.name, "Always Cooperate")

    def test_always_cooperate_strategy_execute(self):
        strategy = AlwaysCooperateStrategy()
        self.assertEqual(strategy.execute(), Action.COOPERATE)


class TestRandomStrategy(unittest.TestCase):
    def test_random_strategy_initialization(self):
        strategy = RandomStrategy()
        self.assertEqual(strategy.name, "Random")

    @patch('random.choice')
    def test_random_strategy_execute_cooperate(self, mock_choice):
        mock_choice.return_value = True
        strategy = RandomStrategy()
        self.assertEqual(strategy.execute(), Action.COOPERATE)

    @patch('random.choice')
    def test_random_strategy_execute_defect(self, mock_choice):
        mock_choice.return_value = False
        strategy = RandomStrategy()
        self.assertEqual(strategy.execute(), Action.DEFECT)


if __name__ == '__main__':
    unittest.main()
