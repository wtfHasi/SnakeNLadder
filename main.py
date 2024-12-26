import pygame
from model import SnakeAndLaddersModel
import random

# Pygame setup
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 10  # 10x10 grid for Snake and Ladder
SQUARE_SIZE = SCREEN_WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake and Ladders")

# Function to draw the board
def draw_board(model):
    # Draw grid
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
    
    # Draw snakes
    for start, end in model.snakes.items():
        start_pos = model.player_agents[0].calculate_new_position(start)
        end_pos = model.player_agents[0].calculate_new_position(end)
        pygame.draw.line(screen, RED, (start_pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2, start_pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2),
                         (end_pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2, end_pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2), 5)

    # Draw ladders
    for start, end in model.ladders.items():
        start_pos = model.player_agents[0].calculate_new_position(start)
        end_pos = model.player_agents[0].calculate_new_position(end)
        pygame.draw.line(screen, GREEN, (start_pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2, start_pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2),
                         (end_pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2, end_pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2), 5)

    # Draw players
    for agent in model.player_agents:
        pos = agent.grid_pos
        pygame.draw.circle(screen, (0, 0, 255), (pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2, (GRID_SIZE - pos[1] - 1) * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
    
    pygame.display.flip()  # Update the screen


# Create initial model instance with the number of players
model = SnakeAndLaddersModel(2)

# Run the model until one player reaches the finish
step_count = 0
running = True
while model.winner is None and running:
    step_count += 1
    print(f"\n--- Step {step_count} ---")
    
    # Handle Pygame events (to allow quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    model.step()  # Advance the game

    # Draw the current state of the board
    draw_board(model)

    # Add a small delay to visualize the game step by step
    pygame.time.delay(1500)  # 1500 milliseconds delay to slow down the simulation

# Announce the winner
if model.winner is not None:
    print(f"\nSimulation Complete. Player {model.winner} wins!")

# After simulation, collect and print the data
df = model.datacollector.get_agent_vars_dataframe()
print(df)

# Quit Pygame
pygame.quit()