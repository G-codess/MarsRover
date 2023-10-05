import logging

# Define cardinal directions, movement rules, and instruction mapping
orient = ['N', 'E', 'S', 'W']
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
instructions = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move_forward'}

# Configure logging settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Rover:
    def __init__(self, x, y, xmax, ymax, bearing, obstacles):
        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.bearing = bearing
        self.obstacles = set(obstacles)

    def move(self, dx, dy, action):
        new_position = (self.x + dx, self.y + dy)

        if new_position not in self.obstacles:
            if 0 <= new_position[0] <= self.xmax and 0 <= new_position[1] <= self.ymax:
                self.x, self.y = new_position
                logging.info(f'Rover moved to ({self.x}, {self.y}) facing {self.bearing}')
            else:
                raise ValueError('Out of bounds, please try again!!')
        else:
            raise ValueError(f'Obstacle detected at {new_position}. Rover cannot {action}!')

    def display_status(self):
        obstacle_status = "No obstacles detected." if not any(
            (self.x + dx, self.y + dy) in self.obstacles for dx, dy in move.values()) else "Obstacle detected."
        print(f"Rover is at ({self.x}, {self.y}) facing {self.bearing}. {obstacle_status}")

class SimpleRover(Rover):
    def turn_right(self):
        self.bearing = orient[(orient.index(self.bearing) + 1) % len(orient)]

    def turn_left(self):
        self.bearing = orient[(orient.index(self.bearing) - 1) % len(orient)]

    def move_forward(self):
        self.move(move[self.bearing][0], move[self.bearing][1], "move")

if __name__ == '__main__':
    try:
        xmax, ymax = map(int, input('Enter grid size (xmax ymax): ').split())
        obstacles = []

        obstacle_count = int(input('Enter the number of obstacles: '))
        for _ in range(obstacle_count):
            obstacle = tuple(map(int, input('Enter obstacle position (x y): ').split()))
            obstacles.append(obstacle)

        x, y, bearing = input('Enter starting coordinates and direction (x y bearing): ').split()
        rover = SimpleRover(int(x), int(y), xmax, ymax, bearing, obstacles)

        commands = input('Enter commands (M for move forward, L for turn left, R for turn right): ')
        for command in commands:
            if command not in 'MRL':
                raise ValueError(f'Invalid instruction "{command}": use M or R or L - please try again')
            else:
                getattr(rover, instructions[command])()

        rover.display_status()

    except ValueError as e:
        logging.error(f'Error: {e}')
