from model import SnakeAndLaddersModel
from agent import PlayerAgent
from mesa.visualization import SolaraViz, make_space_component
import random

def agent_portrayal(agent):
    """Defines how agents are visualized on the grid."""
    if isinstance(agent, PlayerAgent):
        return {
            "Color": "red" if agent.unique_id == 1 else "blue",  # Player 1 is red, Player 2 is blue
            "Shape": "circle",  # Set the shape of the agent
            "r": 0.5,  # Radius of the circle
            "Layer": 1  # Layering to ensure players are above the grid
        }

# Model parameters
model_params = {
    "num_players": 2  # Number of players in the game
}

# Initialize the model with the desired number of players
model1 = SnakeAndLaddersModel(num_players=model_params['num_players'])

# Create the space visualization component
SpaceGraph = make_space_component(agent_portrayal)

# Set up SolaraViz to visualize the model
page = SolaraViz(
    model1,
    components=[SpaceGraph],
    model_params=model_params,
    name="Snake N Ladders Model",
)

# This is required to render the visualization in the Jupyter notebook or local environment
page

# If you want to step through the model and simulate:
for i in range(10):  # Run 10 steps as an example
    model1.step()
    print(f"Step {i+1} completed.")
