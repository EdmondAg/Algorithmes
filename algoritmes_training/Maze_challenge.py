# x = 0  1  2  3  4  5      y
m = [[8, 1, 1, 1, 1, 0],  # 0
     [1, 0, 1, 0, 1, 0],  # 1
     [1, 0, 1, 0, 1, 0],  # 2
     [1, 0, 1, 0, 1, 0],  # 3
     [1, 1, 1, 1, 1, 0],  # 4
     [1, 1, 0, 9, 0, 1]]  # 5


def find_exit(maze, y, x):
    print("Exploring: ", y, x)
    if maze[y][x] == 9:
        for i in maze:
            print(i)
        print(y, x)
        exit(0)

    maze[y][x] = -1

    if x > 0:
        if maze[y][x - 1] >= 1:
            find_exit(maze, y, x - 1)

    if x < len(maze[0]) - 1:
        if maze[y][x + 1] >= 1:
            find_exit(maze, y, x + 1)

    if y > 0:
        if maze[y - 1][x] >= 1:
            find_exit(maze, y - 1, x)

    if y < len(maze) - 1:
        if maze[y + 1][x] >= 1:
            find_exit(maze, y + 1, x)


find_exit(m, 0, 0)
print("Impossible")

