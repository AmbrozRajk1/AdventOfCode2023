from math import gcd

content = [line.replace("\n","") for line in open("day8.txt", encoding="utf8").readlines()]
instructions = content[0]
d = {}
cnt = 0
steps = 0

for line in content[2:]:
    d[line.split('=')[0].strip()] = (line.split('=')[1].strip().split(',')[0].strip().lstrip('('),line.split('=')[1].strip().split(',')[1].strip().rstrip(')'))

currentNodes = [k for k, v in d.items() if k.endswith('A')]
stepsToReachZ = {}

for node in currentNodes:
    currentElement = node
    cnt = 0
    steps = 0

    while not currentElement.endswith('Z'):
        steps += 1
        side = instructions[cnt % len(instructions)]
        cnt += 1
        l, r = d[currentElement]
        if side == 'R':
            currentElement = r
        elif side == 'L':
            currentElement = l

    stepsToReachZ[node] = steps

print(stepsToReachZ)

lcm = 1
for i in stepsToReachZ.values():
    lcm = lcm*i//gcd(lcm, i)
print(lcm)