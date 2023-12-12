from itertools import product

content = [line.replace("\n", "") for line in open("day12.txt", encoding="utf8").readlines()]

def generate_combinations(input_string):
    replacements = ['.', '#']
    question_marks_indices = [i for i, char in enumerate(input_string) if char == '?']
    combinations = product(replacements, repeat=len(question_marks_indices))

    result = []
    for combination in combinations:
        temp_string = list(input_string)
        for index, replacement in zip(question_marks_indices, combination):
            temp_string[index] = replacement
        result.append(''.join(temp_string))

    return result

total = 0
totalLines = len(content)

for cnt, line in enumerate(content):
    read_springs = line.split()[0]
    read_numbers = list(map(int,line.split()[1].split(',')))
    springs = "" + read_springs
    numbers = []

    for i in range(4):
        springs += '?' + read_springs

    for i in range(5):
        for n in read_numbers:
            numbers.append(n)
    print(springs, numbers,"\n")
    # allCombinations = generate_combinations(springs)
    # properCombinations = 0
    #
    # for c in allCombinations:
    #     splitted = c.split('.')
    #     new_splitted = []
    #     for e in splitted:
    #         if len(e) > 0:
    #             new_splitted.append(e)
    #     lenghts = [len(l) for l in new_splitted]
    #
    #     if lenghts == numbers:
    #         properCombinations+=1
    #
    # total += properCombinations
    #
    # print("Finished with {}/{} lines.".format(cnt+1,totalLines))

print(total)