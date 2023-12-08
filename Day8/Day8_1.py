content = [line.replace("\n","") for line in open("day8.txt", encoding="utf8").readlines()]
instructions = content[0]
d = {}
cnt, steps = 0, 0
currentElement = 'AAA'

for line in content[2:]:
    d[line.split('=')[0].strip()] = (line.split('=')[1].strip().split(',')[0].strip().lstrip('('),line.split('=')[1].strip().split(',')[1].strip().rstrip(')'))

while currentElement != 'ZZZ':
    steps += 1
    side = instructions[cnt % len(instructions)]
    cnt += 1
    l, r = d[currentElement]
    if side == 'R':
        currentElement = r
    elif side == 'L':
        currentElement = l

print(steps)