content = [line.replace("\n","") for line in open("day15.txt", encoding="utf8").readlines()]

def getBox(s):
    currentValue = 0
    for c in s:
        currentValue += int(ord(c))
        currentValue *= 17
        currentValue %= 256
    return currentValue

d = {}

for str in content[0].split(','):
    operation = ''
    if '=' in str:
        label, fl = str.split('=')
        operation = 'add'
    if '-' in str:
        label, _ = str.split('-')
        operation = 'remove'

    box = getBox(label)

    if operation == 'add':
        if box not in d:
            d[box] = [label + " " + fl]
        else:
            if any(e.startswith(label + " ") for e in d[box]):
                for i,e in enumerate(d[box]):
                    if e.startswith(label + " "):
                        d[box][i] = label + " " + fl
            else:
                d[box].append(label + " " + fl)

    if operation == 'remove':
        if box in d:
            for e in d[box]:
                if e.startswith(label + " "):
                    d[box].remove(e)

    for key, value in d.items():
        print(f"Box {key}: {value}")
    print()
totalfp = 0

for key, value in d.items():
    for i, e in enumerate(value):
        power = (key+1) * (i+1) * int(e.split()[1])
        totalfp += power

print(totalfp)