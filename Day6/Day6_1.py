import numpy as np

content = [line.replace("\n","") for line in open("day6.txt", encoding="utf8").readlines()]

times = list(map(int,content[0].split(':')[1].strip().split()))
distances = list(map(int,content[1].split(':')[1].strip().split()))
b = []

for i in range(len(times)):
    timeYouHave = times[i]
    currentRecord = distances[i]
    all = {}

    for j in range(timeYouHave+1):
        timeLeft = timeYouHave - j
        distance = timeLeft * j
        all[j] = distance

    b.append(len([v for v in all.values() if int(v) > currentRecord]))
print(np.prod(b))