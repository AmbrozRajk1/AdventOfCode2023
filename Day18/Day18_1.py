import math
import numpy as np

content = [line.replace("\n", "") for line in open("day18.txt", encoding="utf8").readlines()]

coordinates = [(0,0)]
x,y = 0,0
totalCircleLength = 0

for line in content:
    direction, steps, color = line.split()
    totalCircleLength += int(steps)

    if direction == "U":
        x -= int(steps)
    elif direction == "D":
        x += int(steps)
    elif direction == "L":
        y -= int(steps)
    elif direction == "R":
        y += int(steps)

    coordinates.append((x,y))

# calculate area using shoelace algorithm
area = 0

for i in range(len(coordinates) - 1):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i + 1]
    area += ((x1 * y2) - (x2 * y1))

area = abs(area) // 2
inside_points = area - totalCircleLength // 2 + 1

cubicMeters = inside_points + totalCircleLength
print(cubicMeters)