import pygame
import random
from model import SnakeAndLaddersModel

# Set up the pygame screen
WIDTH, HEIGHT = 600, 600  # Size of the window
GRID_SIZE = 10  # 10x10 grid

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Colors for players
PLAYER_COLORS = [RED, BLUE]  # Player 1 and Player 2

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladders")

# Function to draw the grid
def draw_grid():
    cell_width = WIDTH // GRID_SIZE
    cell_height = HEIGHT // GRID_SIZE
    for x in range(0, WIDTH, cell_width):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT), 2)
    for y in range(0, HEIGHT, cell_height):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y), 2)

# Function to draw a player on the board
def draw_player(player, color):
    cell_width = WIDTH // GRID_SIZE
    cell_height = HEIGHT // GRID_SIZE
    col, row = player.grid_pos
    x = col * cell_width + cell_width // 2
    y = (GRID_SIZE - 1 - row) * cell_height + cell_height // 2  # Flip row to keep bottom-left origin
    pygame.draw.circle(screen, color, (x, y), 20)

# Function to render text
def draw_text(text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Function to convert board position to grid coordinates
def position_to_grid(position):
    col = (position - 1) % GRID_SIZE
    row = (position - 1) // GRID_SIZE
    if row % 2 == 1:  # Reverse direction for odd rows
        col = GRID_SIZE - 1 - col
    return (col, row)

# Function to draw snakes and ladders
def draw_snakes_and_ladders(snakes, ladders):
    cell_width = WIDTH // GRID_SIZE
    cell_height = HEIGHT // GRID_SIZE

    # Draw ladders (green)
    for start, end in ladders.items():
        start_col, start_row = position_to_grid(start)
        end_col, end_row = position_to_grid(end)
        start_pos = (start_col * cell_width + cell_width // 2, (GRID_SIZE - 1 - start_row) * cell_height + cell_height // 2)
        end_pos = (end_col * cell_width + cell_width // 2, (GRID_SIZE - 1 - end_row) * cell_height + cell_height // 2)
        pygame.draw.line(screen, GREEN, start_pos, end_pos, 4)

    # Draw snakes (red)
    for start, end in snakes.items():
        start_col, start_row = position_to_grid(start)
        end_col, end_row = position_to_grid(end)
        start_pos = (start_col * cell_width + cell_width // 2, (GRID_SIZE - 1 - start_row) * cell_height + cell_height // 2)
        end_pos = (end_col * cell_width + cell_width // 2, (GRID_SIZE - 1 - end_row) * cell_height + cell_height // 2)
        pygame.draw.line(screen, RED, start_pos, end_pos, 4)

# Create the initial model instance with 2 players
model = SnakeAndLaddersModel(2)

# Set up font for text rendering
font = pygame.font.SysFont('Arial', 24)

# Run the simulation until one player reaches the finish
running = True
step_count = 0
while model.winner is None and running:
    step_count += 1
    print(f"\n--- Step {step_count} ---")
    model.step()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    draw_grid()

    # Draw the snakes and ladders
    draw_snakes_and_ladders(model.snakes, model.ladders)

    # Draw the players
    for i, player in enumerate(model.player_agents):
        draw_player(player, PLAYER_COLORS[i])

    # Draw player status (position and turn)
    for i, player in enumerate(model.player_agents):
        draw_text(f"Player {i+1}: {player.position}", font, PLAYER_COLORS[i], 20, 20 + (i * 30))

    # Check for winner
    if model.winner is not None:
        draw_text(f"Player {model.winner} wins!", font, BLACK, WIDTH // 2 - 100, HEIGHT - 50)

    # Update the screen
    pygame.display.flip()

    # Delay to make game visible (simulation step)
    pygame.time.wait(500)

    # Event handling (to close the window if needed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Simulation complete, announce the winner
print(f"\nSimulation Complete. Player {model.winner} wins!")

# After simulation, collect and print the data
df = model.datacollector.get_agent_vars_dataframe()
print(df)

# Quit pygame when done
pygame.quit()