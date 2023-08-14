from collections import deque


def maze_solver(maze):
    # Initialising variables
    visited = set()
    queue = deque()
    iterations = 0
    result = None
    final = []
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
                queue = deque([(start, '')])  # Giving the que empty set a start value
                break
    # Calculating the position of X
    for p in range(len(maze)):
        for q in range(len(maze[0])):
            if maze[p][q] == 'X':
                maze = variable_positions(maze, p, q)
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
                if (
                        0 <= x < len(maze) and
                        0 <= y < len(maze[0]) and
                        (maze[x][y] & wall_bit) == 0  # Checking if the current cell has walls in the direction
                ):
                    if (nx, ny) == end:  # Terminating the function once 'X' is reached.
                        reached_goal = True
                        result = path + direction  # Getting the shortest available path
                        break
                    elif (  # Calculating available directions
                            (nx, ny) not in visited and
                            0 <= nx < len(maze) and
                            0 <= ny < len(maze[0]) and
                            (maze[nx][ny] & opposite_direction(direction)) == 0
                    ):
                        if path is not None:
                            new_path = path + direction
                        else:
                            new_path = direction
                        queue.append(((nx, ny), new_path))
                        result = new_path

        final = update_final(final, result)
        print(final)

        if reached_goal:
            return list(final)
        else:
            for i in range(len(maze)):
                for j in range(len(maze[0])):
                    rotated_cell = rotate_cell(maze[i][j])
                    maze = update_cell(maze, rotated_cell, i, j)
        queue.append(((x, y), result))
        iterations += 1

    return None
    # No possible solution


# This function moves the ball in the available direction
def move(x, y, direction):
    if direction == 'N':
        return x - 1, y
    if direction == 'W':
        return x, y - 1
    if direction == 'S':
        return x + 1, y
    if direction == 'E':
        return x, y + 1


def opposite_direction(direction):
    if direction == 'N':
        return 2  # Wall_bit for the south direction
    elif direction == 'W':
        return 1  # Wall_bit for the east direction
    elif direction == 'S':
        return 8  # Wall_bit for the north direction
    elif direction == 'E':
        return 4  # Wall_bit for the west direction
    else:
        return 0  # No wall bit


# This function rotates each cell clockwise
def rotate_cell(cell_value):
    return ((cell_value << 1) & 0b1111) | (cell_value >> 3)


# This function updates the values of the maze
def update_cell(maze, rotated_cell, i, j):
    updated_maze = list(maze)
    updated_maze[i] = list(updated_maze[i])
    updated_maze[i][j] = rotated_cell
    updated_maze[i] = tuple(updated_maze[i])
    updated_maze = tuple(updated_maze)
    return updated_maze


# This function sets the variables to zero
def variable_positions(maze, a, b):
    updated_maze = list(maze)
    updated_maze[a] = list(updated_maze[a])
    updated_maze[a][b] = 0
    updated_maze[a] = tuple(updated_maze[a])
    updated_maze = tuple(updated_maze)
    return updated_maze


# This function returns it in the desired format
def update_final(final, new_entry):
    if not final:
        final.append(new_entry)
        return final

    sum_lengths = sum(len(entry) for entry in final if entry is not None)

    updated_entry = ""
    if new_entry is not None:
        for i, char in enumerate(new_entry):
            if i >= sum_lengths:
                updated_entry += char

    final.append(updated_entry)
    return final


# An example set
example = (
    (6, 3, 10, 4, 11),
    (8, 10, 4, 8, 5),
    ('B', 14, 11, 3, 'X'),
    (15, 3, 4, 14, 15),
    (14, 7, 15, 5, 5)
)

print(maze_solver(example))
