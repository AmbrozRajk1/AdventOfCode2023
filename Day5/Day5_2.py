content = open("day5.txt", encoding="utf8").read()
contentList = content.split('\n\n')

seedsRead = [int(x) for x in contentList[0].split(':')[1].strip().split()]
seeds = []
for i in range(0,len(seedsRead)-1,2):
    start = seedsRead[i]
    count = seedsRead[i+1]
    seeds.append((start,start+count))

seedToSoil = []
for l in contentList[1].split('\n')[1:]:
    seedToSoil.append([int(x) for x in l.strip().split()])
soilToFertilizer = []
for l in contentList[2].split('\n')[1:]:
    soilToFertilizer.append([int(x) for x in l.strip().split()])
fertilizerToWater = []
for l in contentList[3].split('\n')[1:]:
    fertilizerToWater.append([int(x) for x in l.strip().split()])
waterToLight = []
for l in contentList[4].split('\n')[1:]:
    waterToLight.append([int(x) for x in l.strip().split()])
lightToTemperature = []
for l in contentList[5].split('\n')[1:]:
    lightToTemperature.append([int(x) for x in l.strip().split()])
temperatureToHumidity = []
for l in contentList[6].split('\n')[1:]:
    temperatureToHumidity.append([int(x) for x in l.strip().split()])
humidityToLocation = []
for l in contentList[7].split('\n')[1:]:
    humidityToLocation.append([int(x) for x in l.strip().split()])

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in seedToSoil:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in soilToFertilizer:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in fertilizerToWater:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in waterToLight:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in lightToTemperature:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in temperatureToHumidity:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

temp = []
while(len(seeds) > 0):
    si, ei = seeds.pop()
    for d, s, r in humidityToLocation:
        overlapS = max(si,s)
        overlapE = min(ei,s+r)

        if overlapS < overlapE:
            temp.append((overlapS-s+d, overlapE-s+d))
            if overlapS > si:
                seeds.append((si,overlapS))
            if ei > overlapE:
                seeds.append((overlapE,ei))
            break
    else:
        temp.append((si,ei))
seeds = temp

print(min(seeds))
