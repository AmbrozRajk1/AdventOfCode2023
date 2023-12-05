content = [line.replace("\n","") for line in open("day4.txt", encoding="utf8").readlines()]

total = 0

for line in content:
    totalCard = 0
    splittedLine = line.split('|')
    splittedLine2 = splittedLine[0].split(':')
    winningNumbers = splittedLine2[1].strip().split()
    yourNumbers = splittedLine[1].strip().split()

    for ynum in yourNumbers:
        if ynum in winningNumbers:
            if totalCard == 0:
                totalCard = 1
            else:
                totalCard *= 2
    total += totalCard

print(total)