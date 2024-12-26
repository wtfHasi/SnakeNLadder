import random
from mesa import Model
import mesa

from agent import PlayerAgent  # Import the agent class

class SnakeAndLaddersModel(Model):
    def __init__(self, num_players):
        super().__init__()
        self.num_players = num_players
        self.grid = mesa.space.MultiGrid(10, 10, torus=False)  # 10x10 board
        self.snakes = {16: 6, 47: 26, 49: 11, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}
        self.ladders = {2: 38, 7: 14, 8: 31, 15: 26, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
        self.winner = None

        # Track player agents explicitly if needed
        self.player_agents = []  # Custom storage, not overwriting model.agents

        # Add players to the model
        for _ in range(self.num_players):
            player = PlayerAgent(self)
            self.player_agents.append(player)  # Keep reference in custom storage
            self.grid.place_agent(player, (0, 0))  # Place agent at the start

    def step(self):
        """Advance the model by one step."""
        random.shuffle(self.player_agents)  # Shuffle players manually
        for agent in self.player_agents:
            agent.step()
