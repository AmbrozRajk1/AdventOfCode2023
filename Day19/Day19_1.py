content = open("day19.txt", encoding="utf8").read()
contentList = content.split('\n\n')

parts = {}
wf = {}

for line in contentList[0].split('\n'):
    wfName, flow = line.split('{')
    wf[wfName] = list(flow.strip('}').split(','))

for i, line in enumerate(contentList[1].split('\n')):
    atts = line.strip('{}').split(',')
    parts[i] = (int(atts[0].split('=')[1]),int(atts[1].split('=')[1]),int(atts[2].split('=')[1]),int(atts[3].split('=')[1]))

acceptedParts = []

for key, part in parts.items():
    x,m,a,s = part
    currentWf = 'in'
    finished = False
    while finished == False:
        for onewf in wf[currentWf]:
            splitedOnewf = onewf.split(':')
            if len(splitedOnewf) == 1:
                currentWf = splitedOnewf[0]
                if currentWf == 'A':
                    acceptedParts.append(part)
                    finished = True
                    break
                elif currentWf == 'R':
                    finished = True
                    break
                else:
                    break
            if len(splitedOnewf) == 2:
                condition, destination = splitedOnewf[0], splitedOnewf[1]
                att = condition[0]
                comparible = condition[1]
                value = int(condition[2:])

                if comparible == '>':
                    if(att == 'x' and x > value) or (att == 'm' and m > value) or (att == 'a' and a > value) or (att == 's' and s > value):
                        currentWf = destination
                    else:
                        continue

                    if currentWf == 'A':
                        acceptedParts.append(part)
                        finished = True
                        break
                    elif currentWf == 'R':
                        finished = True
                        break
                    else:
                        break
                else:
                    if (att == 'x' and x < value) or (att == 'm' and m < value) or (att == 'a' and a < value) or (att == 's' and s < value):
                        currentWf = destination
                    else:
                        continue

                    if currentWf == 'A':
                        acceptedParts.append(part)
                        finished = True
                        break
                    elif currentWf == 'R':
                        finished = True
                        break
                    else:
                        break

total = 0
for p in acceptedParts:
    x, m, a, s = p
    total += x + m + a + s

print(total)