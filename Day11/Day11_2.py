import numpy as np

def getEmptyRows(matrix):
    l = list()
    for i in range(matrix.shape[0]):
        if not np.any(matrix[i] == '#'):
            l.append(i)
    return l

def getEmptyColumns(matrix):
    l = list()
    for i in range(matrix.shape[1]):
        if not np.any(matrix[:,i] == '#'):
            l.append(i)
    return l

def getEmptyRowsBetweenCoordinates(a, b, emptyRows):
    x1, y1 = a
    x2, y2 = b
    cnt = -1

    if x1 <= x2:
        cnt = len([val for val in emptyRows if x1 < val < x2])
    else:
        cnt = len([val for val in emptyRows if x2 < val < x1])

    return cnt

def getEmptyColumnsBetweenCoordinates(a, b, emptyColumns):
    x1, y1 = a
    x2, y2 = b
    cnt = -1

    if y1 <= y2:
        cnt = len([val for val in emptyColumns if y1 < val < y2])
    else:
        cnt = len([val for val in emptyColumns if y2 < val < y1])

    return cnt

content = [line.replace("\n", "") for line in open("day11.txt", encoding="utf8").readlines()]
matrix_data = [list(line) for line in content]
matrix = np.array(matrix_data)

coordinates = set()
alreadyTested = set()

for row in range(matrix.shape[0]):
    for col in range(matrix.shape[1]):
        current_element = matrix[row, col]
        if current_element == '#':
            coordinates.add((row,col))

emptyRows = getEmptyRows(matrix)
emptyColumns = getEmptyColumns(matrix)

totalDistance = 0

for c1 in coordinates:
    for c2 in coordinates:
        if c1 != c2 and (c1,c2) not in alreadyTested and (c2,c1) not in alreadyTested:
            alreadyTested.add((c1,c2))
            r = getEmptyRowsBetweenCoordinates(c1, c2, emptyRows)
            c = getEmptyColumnsBetweenCoordinates(c1, c2, emptyColumns)

            c1x, c1y = c1
            c2x, c2y = c2

            md = abs(c1x - c2x) + abs(c1y - c2y)
            totalDistance += md + r*1000000-r + c*1000000-c

print(totalDistance)