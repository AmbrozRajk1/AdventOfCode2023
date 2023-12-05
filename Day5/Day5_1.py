content = open("day5.txt", encoding="utf8").read()
contentList = content.split('\n\n')

seeds = [int(x) for x in contentList[0].split(':')[1].strip().split()]
all = []

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

for seed in seeds:
    transform = seed
    transformsts = transform
    for d, s, r in seedToSoil:
        if transform >= s and transform < (s+r):
            transformsts = d + (transform-s)
    transformstf = transformsts
    for d, s, r in soilToFertilizer:
        if transformsts >= s and transformsts < (s+r):
            transformstf = d + (transformsts-s)
    transformftw = transformstf
    for d, s, r in fertilizerToWater:
        if transformstf >= s and transformstf < (s+r):
            transformftw = d + (transformstf-s)
    transformwtl = transformftw
    for d, s, r in waterToLight:
        if transformftw >= s and transformftw < (s+r):
            transformwtl = d + (transformftw-s)
    transformltt = transformwtl
    for d, s, r in lightToTemperature:
        if transformwtl >= s and transformwtl < (s+r):
            transformltt = d + (transformwtl-s)
    transformtth = transformltt
    for d, s, r in temperatureToHumidity:
        if transformltt >= s and transformltt < (s+r):
            transformtth = d + (transformltt-s)
    transformhtl = transformtth
    for d, s, r in humidityToLocation:
        if transformtth >= s and transformtth < (s+r):
            transformhtl = d + (transformtth-s)

    all.append(transformhtl)

print(min(all))