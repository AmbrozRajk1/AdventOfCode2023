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

for line in content:
    springs = line.split()[0]
    numbers = list(map(int,line.split()[1].split(',')))

    allCombinations = generate_combinations(springs)
    properCombinations = 0

    for c in allCombinations:
        splitted = c.split('.')
        new_splitted = []
        for e in splitted:
            if len(e) > 0:
                new_splitted.append(e)
        lenghts = [len(l) for l in new_splitted]

        if lenghts == numbers:
            properCombinations+=1

    total += properCombinations

print(total)