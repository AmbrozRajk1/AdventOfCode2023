import numpy as np
from collections import deque

content = [line.replace("\n", "") for line in open("day16.txt", encoding="utf8").readlines()]
matrix_data = [list(line) for line in content]
matrix = np.array(matrix_data)



def is_valid_position(matrix, row, col):
    return 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]

def move(x, y, nx, ny):
    alreadyVisited = set()
    queue = deque()
    queue.append((x, y, nx, ny))

    while queue:
        x, y, nx, ny = queue.popleft()

        x += nx
        y += ny

        if is_valid_position(matrix, x, y) == False:
            continue

        currentElement = matrix[x, y]

        if currentElement == '.' or (currentElement == '-' and nx == 0 and (ny == 1 or ny == -1)) or (
                currentElement == '|' and (nx == 1 or nx == -1) and ny == 0):
            if (x, y, nx, ny) not in alreadyVisited:
                alreadyVisited.add((x, y, nx, ny))
                queue.append((x, y, nx, ny))
        elif currentElement == '/':
            if nx == 0 and ny == 1:
                nx = -1
                ny = 0
            elif nx == 0 and ny == -1:
                nx = 1
                ny = 0
            elif nx == 1 and ny == 0:
                nx = 0
                ny = -1
            elif nx == -1 and ny == 0:
                nx = 0
                ny = 1
            if (x, y, nx, ny) not in alreadyVisited:
                alreadyVisited.add((x, y, nx, ny))
                queue.append((x, y, nx, ny))
        elif currentElement == '\\':
            if nx == 0 and ny == 1:
                nx = 1
                ny = 0
            elif nx == 0 and ny == -1:
                nx = -1
                ny = 0
            elif nx == 1 and ny == 0:
                nx = 0
                ny = 1
            elif nx == -1 and ny == 0:
                nx = 0
                ny = -1
            if (x, y, nx, ny) not in alreadyVisited:
                alreadyVisited.add((x, y, nx, ny))
                queue.append((x, y, nx, ny))
        elif currentElement == '-':
            if (x, y, 0, -1) not in alreadyVisited:
                alreadyVisited.add((x, y, 0, -1))
                queue.append((x, y, 0, -1))
            if (x, y, 0, 1) not in alreadyVisited:
                alreadyVisited.add((x, y, 0, 1))
                queue.append((x, y, 0, 1))
        elif currentElement == '|':
            if (x, y, -1, 0) not in alreadyVisited:
                alreadyVisited.add((x, y, -1, 0))
                queue.append((x, y, -1, 0))
            if (x, y, 1, 0) not in alreadyVisited:
                alreadyVisited.add((x, y, 1, 0))
                queue.append((x, y, 1, 0))

    # remove duplicated coordinates
    setAlreadyVisited = set()
    for x, y, nx, ny in alreadyVisited:
        if (x, y) not in alreadyVisited:
            setAlreadyVisited.add((x, y))

    return len(setAlreadyVisited)

max_energized = 0

for i in range(matrix.shape[0]):
    max_energized = max(max_energized, move(i, -1, 0, 1))
    max_energized = max(max_energized, move(i, matrix.shape[0], 0, -1))
for i in range(matrix.shape[1]):
    max_energized = max(max_energized, move(-1, i, 1, 0))
    max_energized = max(max_energized, move(matrix.shape[1], i, -1, 0))

print(max_energized)