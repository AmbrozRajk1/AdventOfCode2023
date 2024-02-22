content = [line.replace("\n","") for line in open("day9.txt", encoding="utf8").readlines()]

total = 0

for line in content:
    numbers = list(map(int,line.split()))
    allTogether = []
    allTogether.append(numbers.copy())

    while all(n == 0 for n in numbers) == False:
        t = numbers.copy()
        numbers.clear()
        for i in range(len(t)-1):
            numbers.append(t[i+1]-t[i])
        allTogether.append(numbers.copy())

    first = True
    for i in range(len(allTogether) - 1, -1, -1):
        if first:
            allTogether[i].insert(0, 0)
            first = False
        else:
            allTogether[i].insert(0, allTogether[i][0] - allTogether[i+1][0])

    total += allTogether[0][0]
print(total)