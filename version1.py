from collections import deque


def maze_solver(maze):
    # Initialising variables
    visited = set()
    queue = deque()
    iterations = 0
    result = None
    end = None
    reached_goal = False
    directions = ['N', 'W', 'S', 'E']
    wall_bits = [8, 4, 2, 1]

    # Calculating the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'B':
                start = (i, j)
                maze = variable_positions(maze, i, j)
                print(maze)
                queue = deque([(start, '')])  # Giving the que empty set a start value
                break
    # Calculating the position of X
    for p in range(len(maze)):
        for q in range(len(maze[0])):
            if maze[p][q] == 'X':
                maze = variable_positions(maze, p, q)
                print(maze)
                end = (p, q)
                break
    # If the user gives no starting position the program ends here
    if end is None:
        return None

    while iterations <= 20:
        while queue:
            (x, y), path = queue.popleft()  # Getting the co-ordinates of the current position and path travelled
            visited.add((x, y))
            if (x, y) == end:
                break
            for direction, wall_bit in zip(directions, wall_bits):
                nx, ny = move(x, y, direction)
                if (maze[x][y] & wall_bit) == 0:  # Checking if the current cell has walls in the direction
                    if (nx, ny) == end:  # Terminating the function once 'X' is reached.
                        reached_goal = True
                        result = path + direction  # Getting the shortest available path
                        break
                    elif (  # Calculating available directions
                            (nx, ny) not in visited and
                            0 <= nx < len(maze) and
                            0 <= ny < len(maze[0]) and
                            (maze[nx][ny] & wall_bit) == 0
                    ):

                        print(maze[nx][ny])
                        new_path = path + direction
                        queue.append(((nx, ny), new_path))
                        visited.add((nx, ny))
                        result = new_path

        if reached_goal:
            return list(result)
        else:
            rotated_cell = rotate_cell(maze[nx][ny])
            print(rotated_cell)
            maze = update_cell(maze, rotated_cell, nx, ny)
            print(maze)
            iterations += 1
            queue.append(((nx, ny), new_path))
            print(queue)

    return None
    # No possible solution


def move(x, y, direction):  # This function moves the ball in the available direction

    if direction == 'N':
        return x - 1, y
    if direction == 'W':
        return x, y - 1
    if direction == 'S':
        return x + 1, y
    if direction == 'E':
        return x, y + 1


# This function rotates each cell clockwise
def rotate_cell(cell_value):
    print(((cell_value << 1) & 0b1111) | (cell_value >> 3))
    return ((cell_value << 1) & 0b1111) | (cell_value >> 3)


# This function updates the values of the maze
def update_cell(maze, rotated_cell, nx, ny):
    updated_maze = list(maze)
    updated_maze[nx] = list(updated_maze[nx])
    updated_maze[nx][ny] = rotated_cell
    updated_maze[nx] = tuple(updated_maze[nx])
    updated_maze = tuple(updated_maze)
    return updated_maze


def variable_positions(maze, a, b):
    updated_maze = list(maze)
    updated_maze[a] = list(updated_maze[a])
    updated_maze[a][b] = 0
    updated_maze[a] = tuple(updated_maze[a])
    updated_maze = tuple(updated_maze)
    return updated_maze


# An example set
example = (
    (4, 2, 5, 4),
    (4, 15, 11, 1),
    ('B', 9, 6, 8),
    (12, 7, 7, 'X')
)

print(maze_solver(example))
