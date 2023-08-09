from collections import deque


def maze_solver(maze):
    # Initialising variables
    visited = set()
    queue = deque()
    result = None
    end = None
    reached_goal = False

    # Calculating the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'B':
                start = (i, j)
                queue = deque([(start, '')])  # Giving the que empty set a start value
                break
    # Calculating the position of X
    for p in range(len(maze)):
        for q in range(len(maze[0])):
            if maze[p][q] == 'X':
                end = (p, q)
                break
    # If the user gives no starting position the program ends here
    if end is None:
        return None

    def move(x, y, direction):  # This function moves the ball in the available direction

        if direction == 'N':
            return x - 1, y
        if direction == 'W':
            return x, y - 1
        if direction == 'S':
            return x + 1, y
        if direction == 'E':
            return x, y + 1

    while queue:
        (x, y), path = queue.popleft()  # Getting the co-ordinates of the current position and path travelled
        visited.add((x, y))

        for direction, wall_bit in zip(['N', 'W', 'S', 'E'], [8, 4, 2, 1]):
            nx, ny = move(x, y, direction)
            if (nx, ny) == end:  # Terminating the function once 'X' is reached.
                reached_goal = True
                break
            elif (  # Calculating available directions
                    0 <= nx < len(maze) and
                    0 <= ny < len(maze[0]) and
                    (nx, ny) not in visited

            ):  # Making a check for walls using Binary data
                if (maze[nx][ny] & wall_bit) == 0:
                    new_path = path + direction
                    queue.append(((nx, ny), new_path))
                    visited.add((nx, ny))
                    result = new_path  # Getting the shortest available path

    if reached_goal:
        return list(result)
    else:
        return None  # No possible solution


# An example set
example = (
    ('B', 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 14, 'X')
)

print(maze_solver(example))
