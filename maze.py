from collections import deque

visited = set()
que = deque()
result = []


def maze_solver(maze):
    global que
    global result
    # Calculating the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'B':
                start = (i, j)
                que = deque([(start, '')])  # Giving the que empty set a start value
                break

    def move(x, y, direction):  # This function moves the ball in the available direction
        if direction == 'N':
            return x - 1, y
        if direction == 'W':
            return x, y - 1
        if direction == 'S':
            return x + 1, y
        if direction == 'E':
            return x, y + 1

    while que:
        (x, y), path = que.popleft()
        visited.add((x, y))

        for direction, wall_bit in zip(['N', 'W', 'S', 'E'], [8, 4, 2, 1]): 
            nx, ny = move(x, y, direction)
            if (
                    0 <= nx < len(maze) and
                    0 <= ny < len(maze[0]) and
                    isinstance(maze[nx][ny], int) and
                    (nx, ny) not in visited
            ):  #Checking for walls using binary codes
                if (maze[nx][ny] & wall_bit) == 0: 
                    new_path = path + direction
                    que.append(((nx, ny), new_path))
                    visited.add((nx, ny))
                    result = new_path

    if result:
        return list(result)
    else:
        return None  # No possible solution


example = (
    ('B', 2, 5, 4),
    (4, 15, 11, 5),
    (10, 9, 6, 8),
    (12, 20, 7, 'X')
)

print(maze_solver(example))
