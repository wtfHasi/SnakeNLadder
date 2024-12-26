# app.py contains vizualization tools that can only be used in jupyter notebook enviroment
from mesa.visualization import SolaraViz, make_space_component
from model import SnakeAndLaddersModel
from agent import PlayerAgent

# Visualization component for players
def agent_portrayal(agent):
    if isinstance(agent, PlayerAgent):
        return {
            "Shape": "circle",
            "Color": "red" if agent.unique_id == 0 else "blue",  # Red for player 1, Blue for player 2
            "Filled": "true",
            "r": 0.5,  # Radius of the circle
            "Layer": 1  # Layering to ensure players are above the grid
        }

SpaceGraph = make_space_component(agent_portrayal)

model_params = {
    "num_players": 2  # Default number of players
}

# Instantiate the model
model1 = SnakeAndLaddersModel(num_players=2)

# Set up the visualization page
page = SolaraViz(
    model1,
    components=[SpaceGraph],
    model_params=model_params,
    name="Snake N Ladders Model"
)

# This is required to render the visualization
page

