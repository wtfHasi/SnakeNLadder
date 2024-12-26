import mesa
import random

class PlayerAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.position = 1  # Start at position 1 (bottom-left of the board)
        self.grid_pos = (0, 0)  # Start at (0, 0)
        self.dice_value = 0  # Initialize dice value

    def roll_dice(self):
        """Roll a dice and update the dice_value attribute."""
        self.dice_value = random.randint(1, 6)
        return self.dice_value

    def calculate_new_position(self, new_position):
        """Convert board position to grid coordinates."""
        row = (new_position - 1) // 10
        col = (new_position - 1) % 10
        if row % 2 == 1:  # Reverse direction for odd rows
            col = 9 - col
        return (col, row)

    def move(self):
        """Move the player based on dice roll and handle snakes/ladders."""
        dice_roll = self.roll_dice()
        
        # Calculate new position
        new_position = self.position + dice_roll
        if new_position > 100:
            new_position = self.position  # Stay in the same position if roll exceeds 100

        # Check for snakes or ladders
        if new_position in self.model.snakes:
            print(f"Player {self.unique_id} encountered a snake at {new_position}! Sliding down...")
            new_position = self.model.snakes[new_position]
        elif new_position in self.model.ladders:
            print(f"Player {self.unique_id} climbed a ladder at {new_position}!")
            new_position = self.model.ladders[new_position]

        # Update position and grid
        self.position = new_position
        self.grid_pos = self.calculate_new_position(new_position)

        # Move agent in the grid
        self.model.grid.move_agent(self, self.grid_pos)
        print(f"Player {self.unique_id} rolled {dice_roll} and moved to position {self.position} ({self.grid_pos})")

    def step(self):
        """Define the player's actions for each step."""
        if self.model.winner is None:  # Only proceed if there's no winner yet
            self.move()
            if self.position == 100:
                print(f"Player {self.unique_id} wins!")
                self.model.winner = self.unique_id
                self.model.running = False  # End the simulation
