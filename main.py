from model import SnakeAndLaddersModel

# Number of players (can be modified)
num_players = 2

# Create initial model instance with the number of players
model = SnakeAndLaddersModel(num_players=num_players)

# Run the model until one player reaches the finish
step_count = 0
while model.winner is None:
    step_count += 1
    print(f"\n--- Step {step_count} ---")
    model.step()

# Announce the winner
print(f"\nSimulation Complete. Player {model.winner} wins!")

# After simulation, collect and print the data
df = model.datacollector.get_agent_vars_dataframe()
print(df)
