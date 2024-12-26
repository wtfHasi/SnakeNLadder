from model import SnakeAndLaddersModel

# Create initial model instance with 2 players
model1 = SnakeAndLaddersModel(num_players=2)

# Run the model for a few steps to see the output
print("Starting Simulation...\n")
for i in range(5):  # Run 5 steps
    print(f"\n--- Step {i+1} ---")
    model1.step()

print("\nSimulation Complete.")
