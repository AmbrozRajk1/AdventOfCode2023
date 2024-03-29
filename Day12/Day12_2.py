from itertools import product
from functools import cache

@cache
def arrangements(springs,numbers):
    if springs == "":
        return 1 if numbers == () else 0

    if numbers == ():
        return 0 if "#" in springs else 1

    rtn = 0

    if springs[0] in ".?":
        rtn += arrangements(springs[1:], numbers)

    if springs[0] in "#?":
        if numbers[0] <= len(springs) and "." not in springs[:numbers[0]] and (numbers[0] == len(springs) or springs[numbers[0]] != "#"):
            rtn += arrangements(springs[numbers[0] + 1:], numbers[1:])

    return rtn

content = [line.replace("\n", "") for line in open("day12.txt", encoding="utf8").readlines()]

total = 0

for line in content:
    read_springs = line.split()[0]
    read_numbers = list(map(int,line.split()[1].split(',')))
    springs = "" + read_springs
    numbers = []

    for i in range(4):
        springs += '?' + read_springs

    for i in range(5):
        for n in read_numbers:
            numbers.append(n)

    numbers = tuple(numbers)


    total += arrangements(springs, numbers)

print(total)