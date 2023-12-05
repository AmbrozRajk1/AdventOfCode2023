content = [line.replace("\n","") for line in open("day4.txt", encoding="utf8").readlines()]

cards = {}

for line in content:
    totalWins = 0
    splittedLine = line.split('|')
    splittedLine2 = splittedLine[0].split(':')
    cardID = int(splittedLine2[0].split()[-1])
    winningNumbers = splittedLine2[1].strip().split()
    yourNumbers = splittedLine[1].strip().split()

    if cardID in cards:
        cards[cardID] += 1
    else:
        cards[cardID] = 1

    for ynum in yourNumbers:
        if ynum in winningNumbers:
            totalWins += 1
    for i in range(1, totalWins+1):
        if cardID + i in cards:
            cards[cardID + i] += 1
        else:
            cards[cardID + i] = 1

    #process copy cards
    if cards[cardID] > 1:
        for i in range(cards[cardID]-1):
            for i in range(1, totalWins + 1):
                if cardID + i in cards:
                    cards[cardID + i] += 1
                else:
                    cards[cardID + i] = 2

print(sum(cards.values()))

