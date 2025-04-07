# This code is a simple implementation of the Prisoner's Dilemma game
# using different strategies. It includes two strategies: Always Cooperate and Random.
# The game is played for 10 rounds, and the scores are calculated based on the actions of the players.
# The game ends with the final scores of both players.

import random
from enum import Enum

class Action(Enum):
    COOPERATE = 1
    DEFECT = 2

class Strategy:
    def __init__(self, name):
        self.name = name
        self.cumulative_score = 0

    def execute(self):
        raise NotImplementedError("You should implement this method in subclasses")

class AlwaysCooperateStrategy(Strategy):
    def __init__(self):
        super().__init__("Always Cooperate")

    def execute(self):
        return Action.COOPERATE

class RandomStrategy(Strategy):
    def __init__(self):
        super().__init__("Random")

    def execute(self):
        return random.choice([Action.COOPERATE, Action.DEFECT])

class AlwaysDefectStrategy(Strategy):
    def __init__(self):
        super().__init__("Always Defect")
    def execute(self):
        return Action.DEFECT        


def reward(player1Action, player2Action):
    if player1Action == player2Action == Action.COOPERATE:
        return 3, 3
    elif player1Action == Action.COOPERATE and player2Action == Action.DEFECT:
        return 0, 5
    elif player1Action == Action.DEFECT and player2Action == Action.COOPERATE:
        return 5, 0
    elif player1Action == player2Action == Action.DEFECT:
        return 1, 1
    else:
        raise ValueError("Invalid actions")

def play_game(player1_strategy, player2_strategy):
    # log to console that the gane is starting
    print(f"Starting game between {player1_strategy.name} and {player2_strategy.name}")
    for i in range(10):
        player1_action = player1_strategy.execute()
        player2_action = player2_strategy.execute()
        player1_score, player2_score = reward(player1_action, player2_action)
        print(f"Round {i + 1}: {player1_strategy.name} chose {player1_action.name}, {player2_strategy.name} chose {player2_action.name}")
        print(f"Scores: {player1_strategy.name} {player1_score}, {player2_strategy.name} {player2_score}")
        #Calculate cumulative score
        player1_strategy.cumulative_score += player1_score
        player2_strategy.cumulative_score += player2_score
        print(f"Cumulative Scores: {player1_strategy.name} {player1_strategy.cumulative_score}, {player2_strategy.name} {player2_strategy.cumulative_score}")
        print("-" * 40)
    print(f"Ending game between {player1_strategy.name} and {player2_strategy.name}")
    print(f"Final Scores: {player1_strategy.name} {player1_strategy.cumulative_score}, {player2_strategy.name} {player2_strategy.cumulative_score}")
    print("=" * 40)

def codeToStrategy(code):
    if code == 'c':
        return AlwaysCooperateStrategy()
    if code == 'r':
        return RandomStrategy()
    if code == 'd':
        return AlwaysDefectStrategy()
    raise ValueError("Invalid strategy name")

if __name__ == "__main__":
    # Ask the two players for their strategies
    input1 = input("Enter the strategy for the first player (c for cooperate, r for random, d for defect): ")
    # Check if the input is valid
    if input1[0].lower() not in ['c', 'r', 'd']:
        print("Invalid strategy name")
        exit(1)
    # Convert the input to a strategy
    player1_strategy = codeToStrategy(input1[0].lower())
    input2 = input("Enter the strategy for the second player (c for cooperate, r for random, d for defect): ")
    # Check if the input is valid
    if input2[0].lower() not in ['c', 'r', 'd']:
        print("Invalid strategy name")
        exit(1)
    # Convert the input to a strategy
    player2_strategy = codeToStrategy(input2[0].lower())
    # Play the game
    play_game(player1_strategy, player2_strategy)