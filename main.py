import pygame
import random
from model import SnakeAndLaddersModel
import settings  # Import the settings from the settings.py file

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Snake and Ladders")

# Set up font for text rendering
font = pygame.font.SysFont(settings.FONT_NAME, settings.FONT_SIZE)

# Function to draw the grid and number the cells
def draw_grid():
    cell_width = settings.WIDTH // settings.GRID_SIZE
    cell_height = settings.HEIGHT // settings.GRID_SIZE
    number = 1

    # Loop through the rows and columns
    for row in range(settings.GRID_SIZE - 1, -1, -1):  # Iterate rows from bottom to top
        if row % 2 == 0:  # Even rows (start from the right)
            for col in range(settings.GRID_SIZE - 1, -1, -1):
                x = col * cell_width + cell_width // 2
                y = row * cell_height + cell_height // 2
                text = font.render(str(number), True, (0, 0, 0))
                screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
                number += 1
        else:  # Odd rows (start from the left)
            for col in range(settings.GRID_SIZE):
                x = col * cell_width + cell_width // 2
                y = row * cell_height + cell_height // 2
                text = font.render(str(number), True, (0, 0, 0))
                screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
                number += 1

    # Draw the grid lines
    for x in range(0, settings.WIDTH, cell_width):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, settings.HEIGHT), 2)
    for y in range(0, settings.HEIGHT, cell_height):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (settings.WIDTH, y), 2)

# Function to draw a player on the board
def draw_player(player, color):
    cell_width = settings.WIDTH // settings.GRID_SIZE
    cell_height = settings.HEIGHT // settings.GRID_SIZE
    col, row = player.grid_pos
    x = col * cell_width + cell_width // 2
    y = (settings.GRID_SIZE - 1 - row) * cell_height + cell_height // 2  # Flip row to keep bottom-left origin
    pygame.draw.circle(screen, color, (x, y), 20)

# Function to render text
def draw_text(text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Function to convert board position to grid coordinates
def position_to_grid(position):
    col = (position - 1) % settings.GRID_SIZE
    row = (position - 1) // settings.GRID_SIZE
    if row % 2 == 1:  # Reverse direction for odd rows
        col = settings.GRID_SIZE - 1 - col
    return (col, row)

# Function to draw snakes and ladders
def draw_snakes_and_ladders(snakes, ladders):
    cell_width = settings.WIDTH // settings.GRID_SIZE
    cell_height = settings.HEIGHT // settings.GRID_SIZE

    # Draw ladders (green)
    for start, end in ladders.items():
        start_col, start_row = position_to_grid(start)
        end_col, end_row = position_to_grid(end)
        start_pos = (start_col * cell_width + cell_width // 2, (settings.GRID_SIZE - 1 - start_row) * cell_height + cell_height // 2)
        end_pos = (end_col * cell_width + cell_width // 2, (settings.GRID_SIZE - 1 - end_row) * cell_height + cell_height // 2)
        pygame.draw.line(screen, (0, 255, 0), start_pos, end_pos, 4)

    # Draw snakes (red)
    for start, end in snakes.items():
        start_col, start_row = position_to_grid(start)
        end_col, end_row = position_to_grid(end)
        start_pos = (start_col * cell_width + cell_width // 2, (settings.GRID_SIZE - 1 - start_row) * cell_height + cell_height // 2)
        end_pos = (end_col * cell_width + cell_width // 2, (settings.GRID_SIZE - 1 - end_row) * cell_height + cell_height // 2)
        pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 4)

# Create the initial model instance with 2 players
model = SnakeAndLaddersModel(2)

# Clear the screen and draw the initial state
screen.fill((255, 255, 255))  # Fill with white before drawing any elements
draw_grid()  # Draw the grid
draw_snakes_and_ladders(model.snakes, model.ladders)  # Draw the snakes and ladders

# Draw players
for i, player in enumerate(model.player_agents):
    draw_player(player, settings.PLAYER_COLORS['player1'] if i == 0 else settings.PLAYER_COLORS['player2'])

# Update the screen immediately to show the initial state
pygame.display.flip()

# Run the simulation until one player reaches the finish
running = True
while model.winner is None and running:
    # Prompt user to "roll" before each step
    draw_text("Press ENTER to roll the dice.", font, (0, 0, 0), settings.WIDTH // 2 - 100, settings.HEIGHT - 50)

    # Wait for user input (pressing ENTER to roll)
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting_for_input = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_input = False
                model.step()  # Invoke the next step

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid with numbered cells
    draw_grid()

    # Draw the snakes and ladders
    draw_snakes_and_ladders(model.snakes, model.ladders)

    # Draw the players
    for i, player in enumerate(model.player_agents):
        draw_player(player, settings.PLAYER_COLORS['player1'] if i == 0 else settings.PLAYER_COLORS['player2'])

    # Check for winner
    if model.winner is not None:
        draw_text(f"Player {model.winner} wins!", font, (0, 0, 0), settings.WIDTH // 2 - 100, settings.HEIGHT - 50)

    # Update the screen
    pygame.display.flip()

# Simulation complete, announce the winner
print(f"\nSimulation Complete. Player {model.winner} wins!")

# Quit pygame when done
pygame.quit()
