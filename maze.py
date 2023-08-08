from collections import deque

visited = set()
que = deque()
result = []
end = None


def maze_solver(maze):
    global que, result, end

    # Calculating the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'B':
                start = (i, j)
                que = deque([(start, '')])  # Giving the que empty set a start value
                break
    # Calculating the psotion of X
    for p in range(len(maze)):
        for q in range(len(maze[0])):
            if maze[p][q] == 'X':
                end = (p, q)
                break

    def move(x, y, direction):  # This function moves the ball in the available direction
        if (x, y) != end:
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
                    (nx, ny) not in visited and
                    (nx, ny) != end
            ):
                print(nx, ny)
                print(maze[nx][ny])
                if (maze[nx][ny] & wall_bit) == 0:
                    new_path = path + direction
                    print(new_path)
                    que.append(((nx, ny), new_path))
                    visited.add((nx, ny))
                    result.append(new_path)

                else:
                    return list(result)


example = (
    (4, 2, 5, 4),
    (4, 15, 11, 1),
    ('B', 9, 6, 8),
    (12, 7, 7, 'X')
)

print(maze_solver(example))
