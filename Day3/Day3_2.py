import numpy as np

def is_valid_position(matrix, row, col):
    return 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]

def count_neighbors(matrix, row, col, totalCount, alreadyVisited):
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
    neighbors = []
    nums = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_position(matrix, new_row, new_col) and matrix[new_row, new_col].isnumeric() and (new_row,new_col) not in alreadyVisited:
            num = get_full_number(matrix,new_row, new_col)
            nums.append(num)

    if len(nums) == 2:
        totalCount = totalCount + (nums[0] * nums[1])

    return totalCount, alreadyVisited

def get_full_number(matrix, row, col):
    current_element = matrix[row, col]
    l=[]
    l.append(current_element)
    alreadyVisited.append((row, col))

    leftIndex = col - 1
    rightIndex = col + 1

    s = matrix[row, leftIndex]

    while is_valid_position(matrix,row,leftIndex) and matrix[row,leftIndex].isnumeric():
        l.insert(0, matrix[row,leftIndex])
        alreadyVisited.append((row,leftIndex))
        leftIndex = leftIndex - 1

    while is_valid_position(matrix,row,rightIndex) and matrix[row,rightIndex].isnumeric():
        l.append(matrix[row,rightIndex])
        alreadyVisited.append((row, rightIndex))
        rightIndex = rightIndex + 1

    return int(''.join(l))

def sum_part_numbers(matrix, totalCount, alreadyVisited):
    part_numbers_sum = 0

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            current_element = matrix[row, col]

            if current_element in ['*']:
                totalCount, alreadyVisited = count_neighbors(matrix, row, col, totalCount, alreadyVisited)

    return totalCount

content = [line.replace("\n", "") for line in open("day3.txt", encoding="utf8").readlines()]
matrix_data = [list(line) for line in content]
matrix = np.array(matrix_data)
totalCount = 0
alreadyVisited = []

result = sum_part_numbers(matrix, totalCount, alreadyVisited)
print(result)