# Import the logging module to handle logging information
import logging

# Define cardinal directions, movement rules, and instruction mapping
orient = ['N', 'E', 'S', 'W']
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
instructions = {'L': 'tleft', 'R': 'tright', 'M': 'move'}

# Configure logging settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Rover class
class Rover:
    def __init__(self, x, y, xmax, ymax, bearing, obstacles):
        # Initialize Rover with initial position, grid boundaries, direction, and obstacles
        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.bearing = bearing
        self.obstacles = set(obstacles)

    def tright(self):
        # Turn the Rover to the right
        self.bearing = orient[(orient.index(self.bearing) + 1) % len(orient)]

    def tleft(self):
        # Turn the Rover to the left
        self.bearing = orient[(orient.index(self.bearing) - 1) % len(orient)]

    def move(self):
        # Move the Rover based on its current direction
        xmod = self.x + move[self.bearing][0]
        ymod = self.y + move[self.bearing][1]
        new_position = (xmod, ymod)

        # Check for obstacles and boundaries before moving
        if new_position not in self.obstacles:
            if 0 <= xmod <= self.xmax and 0 <= ymod <= self.ymax:
                self.x = xmod
                self.y = ymod
                logging.info(f'Rover moved to ({self.x}, {self.y}) facing {self.bearing}')
            else:
                raise ValueError('Out of bounds, please try again!!')
        else:
            raise ValueError(f'Obstacle detected at {new_position}. Rover cannot move!')

# Main program execution
if __name__ == '__main__':
    try:
        # User input for grid size and obstacles
        xmax, ymax = map(int, input('Enter grid size (xmax ymax): ').split())
        obstacles = []

        # User input for obstacle positions
        obstacle_count = int(input('Enter the number of obstacles: '))
        for _ in range(obstacle_count):
            obstacle = tuple(map(int, input('Enter obstacle position (x y): ').split()))
            obstacles.append(obstacle)

        # User input for starting position and direction
        x, y, bearing = input('Enter starting coordinates and direction (x y bearing): ').split()
        rover = Rover(int(x), int(y), xmax, ymax, bearing, obstacles)

        # User input for movement commands
        commands = input('Enter commands (M for move, L for turn left, R for turn right): ')
        for i in commands:
            if i not in 'MRL':
                raise ValueError(f'Invalid instruction "{i}": use M or R or L - please try again')
            else:
                getattr(rover, instructions[i])()

        # Display final position and status report
        print(f"Final Position: ({rover.x}, {rover.y}, {rover.bearing})")

        obstacle_status = "No obstacles detected." if not any((rover.x + dx, rover.y + dy) in rover.obstacles for dx, dy in move.values()) else "Obstacle detected."
        print(f"Status Report: \"Rover is at ({rover.x}, {rover.y}) facing {rover.bearing}. {obstacle_status}\"")

    except ValueError as e:
        logger.error(f'Error: {e}')
