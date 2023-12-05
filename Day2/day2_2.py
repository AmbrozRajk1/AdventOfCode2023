import numpy as np

content = [line.replace("\n","") for line in open("day2.txt", encoding="utf8").readlines()]

availableCubes = {'red': 12, 'green': 13, 'blue': 14}
totalSum = 0

for line in content:
    id = line.split(':')[0].split()[-1]
    sets = line.split(':')[-1].split(';')

    maxNumColors = {'red': 0, 'green': 0, 'blue': 0}

    for s in sets:
        puls = s.split(',')
        for p in puls:
            color = p.split()[-1]
            num = p.split()[0]

            if maxNumColors[color] < int(num):
                maxNumColors[color] = int(num)

    totalSum += np.prod(list(maxNumColors.values()))

print(totalSum)