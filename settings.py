# settings.py

# Colors for players
PLAYER_COLORS = {
    "player1": (255, 0, 0),  # Red for Player 1
    "player2": (0, 0, 255),  # Blue for Player 2
}

# Game settings
GRID_SIZE = 10  # The grid will be 10x10
WIDTH = 600  # Window width
HEIGHT = 600  # Window height

PROMPT_HEIGHT = 50  # Height for the prompt area (you can adjust this value)

# Snakes and ladders setup
SNAKES = {16: 6, 47: 26, 49: 11, 93: 73, 99: 78}
LADDERS = {3: 22, 8: 31, 28: 84, 36: 44, 51: 67}

# Font settings
FONT_NAME = 'Verdana'
FONT_SIZE = 18  # Slightly larger for better readability