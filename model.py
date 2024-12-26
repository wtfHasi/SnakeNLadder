import mesa
from agent import PlayerAgent
import random
from mesa.datacollection import DataCollector

class SnakeAndLaddersModel(mesa.Model):
    def __init__(self, num_players):
        super().__init__()
        self.num_players = num_players
        self.grid = mesa.space.MultiGrid(10, 10, torus=False)  # 10x10 board
        self.snakes = {16: 6, 47: 26, 49: 11, 93: 73, 99: 78}
        self.ladders = {3: 22, 8: 31, 28: 84, 36: 44, 51: 67}
        self.winner = None

        self.player_agents = []  # Custom storage, not overwriting model.agents

        # Add players to the model
        for _ in range(self.num_players):
            player = PlayerAgent(self)
            self.player_agents.append(player)
            self.grid.place_agent(player, (0, 0))  # Place agent at the start
            print(f"Player {player.unique_id} created")  # Verify unique IDs
            
        # Initialize DataCollector
        self.datacollector = DataCollector(
            model_reporters={},
            agent_reporters={
                "Position": lambda agent: agent.position,
                "Dice Value": lambda agent: agent.dice_value
            }
        )

    def step(self):
        """Advance the model by one step."""
        random.shuffle(self.player_agents)  # Shuffle players manually
        for agent in self.player_agents:
            agent.step()
        # Collect data at the end of each step
        self.datacollector.collect(self)