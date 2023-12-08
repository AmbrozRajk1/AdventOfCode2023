content = [line.replace("\n","") for line in open("day7.txt", encoding="utf8").readlines()]
strength = {'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}

cardsCount = len(content)
totalWinings = 0

d5k = {}
d4k = {}
dfh = {}
d3k = {}
d2p = {}
d1p = {}
dhc = {}

for line in content:
    cards = list(line.split()[0])
    bid = int(line.split()[1])

    d1 = {}

    for e in cards:
        if e not in d1:
            d1[e] = 1
        else:
            d1[e] += 1

    if 5 in d1.values():
        d5k["".join(cards)] = bid
    elif 4 in d1.values():
        d4k["".join(cards)] = bid
    elif 3 in d1.values() and 2 in d1.values():
        dfh["".join(cards)] = bid
    elif 3 in d1.values():
        d3k["".join(cards)] = bid
    elif sum(x == 2 for x in d1.values()) == 2:
        d2p["".join(cards)] = bid
    elif sum(x == 2 for x in d1.values()) == 1:
        d1p["".join(cards)] = bid
    else:
        dhc["".join(cards)] = bid

d5kList = []
d4kList = []
dfhList = []
d3kList = []
d2pList = []
d1pList = []
dhcList = []

for k,v in d5k.items():
    d5kList.append((k,v))
for k,v in d4k.items():
    d4kList.append((k,v))
for k,v in dfh.items():
    dfhList.append((k,v))
for k,v in d3k.items():
    d3kList.append((k,v))
for k,v in d2p.items():
    d2pList.append((k,v))
for k,v in d1p.items():
    d1pList.append((k,v))
for k,v in dhc.items():
    dhcList.append((k,v))

allLists = [d5kList, d4kList, dfhList, d3kList, d2pList, d1pList, dhcList]
finalLists = []

for l in allLists:
    #bubble sort each list
    for i in range(len(l)-1):
        for j in range(0,len(l)-i-1):
            e1, b1 = l[j]
            e2, b2 = l[j+1]

            for k in range(len(e2)):
                if strength[e1[k]] > strength[e2[k]]:
                    break
                elif strength[e1[k]] < strength[e2[k]]:
                    tmp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = tmp
                    break
    finalLists.append(l)

for l in finalLists:
    if len(l) > 0:
        for card, bid in l:
            totalWinings += bid * cardsCount
            cardsCount -= 1

print(totalWinings)