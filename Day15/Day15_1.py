content = [line.replace("\n","") for line in open("day15.txt", encoding="utf8").readlines()]
total = 0

for str in content[0].split(','):
    currentValue = 0
    for c in str:
        currentValue += int(ord(c))
        currentValue *= 17
        currentValue %= 256
    total += currentValue
print(total)