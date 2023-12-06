import numpy as np

content = [line.replace("\n","") for line in open("day6.txt", encoding="utf8").readlines()]

times = list(map(int,content[0].split(':')[1].strip().split()))
distances = list(map(int,content[1].split(':')[1].strip().split()))
all = {}

timeYouHave = int(''.join(map(str, times)))
currentRecord = int(''.join(map(str, distances)))

#for j in range(timeYouHave+1):
#    timeLeft = timeYouHave - j
#    distance = timeLeft * j
#    all[j] = distance

#print(len([v for v in all.values() if int(v) > currentRecord]))

#znik solution
def get_x_solutions(time, distance):
    a = -1
    b = time
    c = -distance

    x1 = np.ceil((-b+np.sqrt(b**2-4*a*c))/2*a)
    x2 = np.ceil((-b-np.sqrt(b**2-4*a*c))/2*a)

    return int(x2-x1)

print(get_x_solutions(timeYouHave, currentRecord))