content = [line.replace("\n","") for line in open("day2.txt", encoding="utf8").readlines()]

availableCubes = {'red': 12, 'green': 13, 'blue': 14}
possiblGameIDs = []

for line in content:
    id = line.split(':')[0].split()[-1]
    sets = line.split(':')[-1].split(';')

    gameOK = True
    for s in sets:
        puls = s.split(',')
        for p in puls:
            color = p.split()[-1]
            num = p.split()[0]

            if availableCubes[color] < int(num):
                gameOK = False

    if gameOK:
        possiblGameIDs.append(int(id))

print(sum(possiblGameIDs))