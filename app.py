from mesa.visualization import SolaraViz, make_space_component
from model import SnakeAndLaddersModel
from agent import PlayerAgent

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
    "num_players": 2  # Default number of players; can be modified in the visualization
}

# Create initial model instance
model1 = SnakeAndLaddersModel(num_players=2)

# Visualization components
SpaceGraph = make_space_component(agent_portrayal)

# Create the page
page = SolaraViz(
    model1,
    components=[SpaceGraph],
    model_params=model_params,
    name="Snake N Ladders Model",
)

# This is required to render the visualization in the Jupyter notebook
page
