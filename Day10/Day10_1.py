import numpy as np

def is_valid_position(matrix, row, col):
    return 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]

def getValidNeigbour(matrix, row, col, alreadyVisited, verticalUpValidMoves, verticalDownValidMoves, horizontalRightValidMoves, horizontalLeftValidMoves):
    currentElement = matrix[row,col]

    if is_valid_position(matrix, row-1, col) and matrix[row-1,col] in ('|','7','F') and (row-1,col) not in alreadyVisited and matrix[row-1, col] in verticalUpValidMoves[currentElement]:
        return (matrix[row-1, col],(row-1, col))
    elif is_valid_position(matrix, row+1, col) and matrix[row+1,col] in ('|','L','J') and (row+1,col) not in alreadyVisited and matrix[row+1, col] in verticalDownValidMoves[currentElement]:
        return (matrix[row+1, col], (row+1, col))
    elif is_valid_position(matrix, row, col-1) and matrix[row,col-1] in ('-','F','L') and (row,col-1) not in alreadyVisited and matrix[row, col-1] in horizontalLeftValidMoves[currentElement]:
        return (matrix[row, col-1], (row, col-1))
    elif is_valid_position(matrix, row, col+1) and matrix[row,col+1] in ('-','7','J') and (row,col+1) not in alreadyVisited and matrix[row, col+1] in horizontalRightValidMoves[currentElement]:
        return (matrix[row, col+1], (row, col+1))
    else:
        return ('S',(-1,-1))

content = [line.replace("\n", "") for line in open("day10.txt", encoding="utf8").readlines()]
matrix_data = [list(line) for line in content]
matrix = np.array(matrix_data)

verticalUpValidMoves = {'S': ['|','7','F'], '|': ['S','|','7','F'], '-': [], 'L': ['S','|','7','F'], 'J': ['S','|','7','F'], '7': [], 'F': []}
verticalDownValidMoves = {'S': ['|','L','J'], '|': ['S','|','L','J'], '-': [], 'L': [], 'J': [], '7': ['S','|','L','J'], 'F': ['S','|','L','J']}
horizontalRightValidMoves = {'S': ['-','J','7'], '|': [], '-': ['S','-','J','7'], 'L': ['S','-','7','J'], 'J': [], '7': [], 'F': ['S','-','7','J']}
horizontalLeftValidMoves = {'S': ['-','L','F'], '|': [], '-': ['S','-','L','F'], 'L': [], 'J': ['S','-','L','F'], '7': ['S','-','L','F'], 'F': []}

new_matrix = np.copy(matrix)
new_matrix[new_matrix != '.'] = '.'

sx, sy = 0, 0
found = False
alreadyVisited = []

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[i,j] == 'S':
            sx = i
            sy = j
            found = True
            break
    if found:
        break

alreadyVisited.append((sx,sy))
new_matrix[sx,sy] = 'S'

totalSteps = 0
newNeigbour, (nx, ny) = getValidNeigbour(matrix, sx, sy, alreadyVisited, verticalUpValidMoves, verticalDownValidMoves, horizontalRightValidMoves, horizontalLeftValidMoves)
alreadyVisited.append((nx,ny))
totalSteps += 1
new_matrix[nx,ny] = newNeigbour

while newNeigbour != 'S':
    newNeigbour, (nx, ny) = getValidNeigbour(matrix, nx, ny, alreadyVisited, verticalUpValidMoves, verticalDownValidMoves, horizontalRightValidMoves, horizontalLeftValidMoves)
    alreadyVisited.append((nx,ny))
    totalSteps += 1
    new_matrix[nx, ny] = newNeigbour

np.set_printoptions(threshold=np.inf, linewidth=np.inf)
for row in new_matrix:
    print(row)
print(totalSteps//2)



