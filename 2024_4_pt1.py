from puzzle_input_4 import input
from test import test_input
import re

pattern = r"XMAS|SAMX"

matrix = [[i for i in line] for line in input.strip().split('\n')]
rows_number = len(matrix)
columns_number = len(matrix[0])

def overlap(string, pattern):
    matches = 0
    start = 0
    while match := re.search(pattern, string[start:]):
        matches += 1
        start += match.start() + 1
    return matches

def check_horizontal(matrix):
    counter = 0
    for i in matrix:
        string = ''.join(i)
        counter += overlap(string, pattern)
    return counter

def check_vertical(matrix):
    counter = 0
    for col in range(columns_number):
        string = ''.join(matrix[row][col] for row in range(rows_number))
        counter += overlap(string, pattern)
    return counter

def check_diagonal(matrix):
    counter = 0

    def get_diagonal(matrix, start_row, start_col, direction):
        diagonal = ''
        row, col = start_row, start_col
        while 0 <= row < rows_number and 0 <= col < columns_number:
            diagonal += matrix[row][col]
            row += direction[0]
            col += direction[1]
        return diagonal

    for col in range(columns_number):
        main_diag = get_diagonal(matrix, 0, col, (1, 1))
        counter += overlap(main_diag, pattern)
        anti_diag = get_diagonal(matrix, 0, col, (1, -1))
        counter += overlap(anti_diag, pattern)

    for row in range(1, rows_number):
        main_diag = get_diagonal(matrix, row, 0, (1, 1))
        counter += overlap(main_diag, pattern)
        anti_diag = get_diagonal(matrix, row, columns_number - 1, (1, -1))
        counter += overlap(anti_diag, pattern)

    return counter

def main():
    horizontal_count = check_horizontal(matrix)
    vertical_count = check_vertical(matrix)
    diagonal_count = check_diagonal(matrix)
    result = horizontal_count + vertical_count + diagonal_count

    print(f"Horizontal: {horizontal_count}, Vertical: {vertical_count}, Diagonal: {diagonal_count}")
    return result

if __name__ == "__main__":
    print(main())



