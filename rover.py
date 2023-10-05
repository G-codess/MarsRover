import logging

orient = ['N', 'E', 'S', 'W']
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
instructions = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move_forward'}

class UserInputValidator:
    @staticmethod
    def validate_grid_size(input_str):
        try:
            xmax, ymax = map(int, input_str.split())
            if xmax <= 0 or ymax <= 0:
                raise ValueError('Grid size must be positive integers.')
            return xmax, ymax
        except ValueError:
            raise ValueError('Invalid grid size format. Please enter positive integers separated by a space.')

    @staticmethod
    def validate_obstacle(input_str):
        try:
            obstacle = tuple(map(int, input_str.split()))
            if len(obstacle) != 2:
                raise ValueError('Invalid obstacle position format. Please enter x and y coordinates separated by a space.')
            return obstacle
        except ValueError:
            raise ValueError('Invalid obstacle position format. Please enter x and y coordinates separated by a space.')

    @staticmethod
    def validate_starting_position(input_str):
        try:
            xcoord, ycoord, direction = input_str.split()
            return int(xcoord), int(ycoord), direction
        except ValueError:
            raise ValueError('Invalid starting position format. Please enter x and y coordinates and a direction separated by spaces.')

    @staticmethod
    def validate_commands(input_str):
        if any(command not in 'MRL' for command in input_str):
            raise ValueError('Invalid command. Use only M, R, or L.')
        return input_str

class Rover:
    def __init__(self, xcoord, ycoord, xmax, ymax, direction, obstacles):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.xmax = xmax
        self.ymax = ymax
        self.direction = direction
        self.obstacles = set(obstacles)

    def move(self, dx, dy, action):
        new_position = (self.xcoord + dx, self.ycoord + dy)

        if new_position not in self.obstacles:
            if 0 <= new_position[0] <= self.xmax and 0 <= new_position[1] <= self.ymax:
                self.xcoord, self.ycoord = new_position
                logging.info(f'Rover moved to ({self.xcoord}, {self.ycoord}) facing {self.direction}')
            else:
                raise ValueError('Out of bounds, please try again!!')
        else:
            raise ValueError(f'Obstacle detected at {new_position}. Rover cannot {action}!')

    def display_status(self):
        obstacle_status = "No obstacles detected." if not any(
            (self.xcoord + dx, self.ycoord + dy) in self.obstacles for dx, dy in move.values()) else "Obstacle detected."
        print(f"Rover is at ({self.xcoord}, {self.ycoord}) facing {self.direction}. {obstacle_status}")

class SimpleRover(Rover):
    def turn_right(self):
        self.direction = orient[(orient.index(self.direction) + 1) % len(orient)]

    def turn_left(self):
        self.direction = orient[(orient.index(self.direction) - 1) % len(orient)]

    def move_forward(self):
        self.move(move[self.direction][0], move[self.direction][1], "move")

def main():
    try:
        xmax, ymax = UserInputValidator.validate_grid_size(input('Enter grid size (xmax ymax): '))
        obstacles = []

        obstacle_count = int(input('Enter the number of obstacles: '))
        for _ in range(obstacle_count):
            obstacle = UserInputValidator.validate_obstacle(input('Enter obstacle position (x y): '))
            obstacles.append(obstacle)

        xcoord, ycoord, direction = UserInputValidator.validate_starting_position(
            input('Enter starting coordinates and direction (x y bearing): '))
        rover = SimpleRover(xcoord, ycoord, xmax, ymax, direction, obstacles)

        commands = UserInputValidator.validate_commands(input('Enter commands (M for move forward, L for turn left, R for turn right): '))
        for command in commands:
            getattr(rover, instructions[command])()

        rover.display_status()

    except ValueError as e:
        logging.error(f'Error: {e}')

if __name__ == '__main__':
    main()