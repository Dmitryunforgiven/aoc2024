from puzzle_input_4 import input
from test import test_input

matrix = [[i for i in line] for line in input.split('\n')]
rows_number = len(matrix)
columns_number = len(matrix[0])
coordinates_list = []
counter = 0
for row_idx, row in enumerate(matrix):
    for col_idx, val in enumerate(row):
        if val == 'A':
            coordinates_list.append([row_idx, col_idx])

coordinates_list = [i for i in coordinates_list if 0 < i[0] < rows_number - 1 and 0 < i[1] < columns_number - 1]

for i in coordinates_list:
    if (matrix[i[0] - 1][i[1] - 1] == 'M' and matrix[i[0] + 1][i[1] + 1] == 'S' and matrix[i[0] - 1][i[1] + 1] == 'S' and matrix[i[0] + 1][i[1] - 1] == 'M'):
        counter += 1
    elif (matrix[i[0] - 1][i[1] - 1] == 'S' and matrix[i[0] + 1][i[1] + 1] == 'M' and matrix[i[0] - 1][i[1] + 1] == 'S' and matrix[i[0] + 1][i[1] - 1] == 'M'):
        counter += 1
    elif (matrix[i[0] - 1][i[1] - 1] == 'M' and matrix[i[0] + 1][i[1] + 1] == 'S' and matrix[i[0] - 1][i[1] + 1] == 'M' and matrix[i[0] + 1][i[1] - 1] == 'S'):
        counter += 1
    elif (matrix[i[0] - 1][i[1] - 1] == 'S' and matrix[i[0] + 1][i[1] + 1] == 'M' and matrix[i[0] - 1][i[1] + 1] == 'M' and matrix[i[0] + 1][i[1] - 1] == 'S'):
        counter += 1

print(counter)

