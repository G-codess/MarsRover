# Mars Rovers

This is a Python program that simulates the movement of rovers on the surface of Mars within a specified grid. The rovers follow user-provided commands to navigate and explore the Martian terrain, taking into account obstacles and grid boundaries.

# Features:

Grid Navigation: Define the size of the grid where the rovers will operate (xmax, ymax).

Obstacle Avoidance: Specify obstacle positions, and the rovers will avoid them during navigation.

Rover Commands: Issue commands to the rovers, including turning left (L), turning right (R), and moving forward (M).

Status Reporting: Get a final position report and a status report indicating whether obstacles were detected.

# Follow the On-Screen Instructions:

>> Enter the grid size (xmax ymax).

>> Enter the number and positions of obstacles.

>> Enter the starting coordinates and direction of the rover.

>> Enter the movement commands (M for move, L for turn left, R for turn right).

For Example :

Enter grid size (xmax ymax): 10 10

Enter the number of obstacles: 2

Enter obstacle position (x y): 2 2

Enter obstacle position (x y):3 5

Enter starting coordinates and direction (x y bearing): 0 0 N

Enter commands (M for move, L for turn left, R for turn right): MMRMLM

# Review the Results:

>> The program will display the final position of the rover.

>> A status report will indicate whether obstacles were detected during the navigation.


Final Position: (1, 3, N)

Status Report: "Rover is at (1, 3) facing N. No obstacles detected."
