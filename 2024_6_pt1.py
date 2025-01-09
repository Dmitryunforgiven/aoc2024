from puzzle_input_6 import input
from test import test_input


matrix =  [i for i in input.split('\n') if i != '']
matrix_len = len(matrix[0])
matrix_height = len(matrix)

step_counter = 1

stops_coordinates = []



for row_idx, row in enumerate(matrix):
    for element_idx, element in enumerate(row):
        if element == '#':
            stops_coordinates.append([element_idx, row_idx])
        elif element == '^':
            start_coordinates = [element_idx, row_idx]

visited_coordinates = stops_coordinates + [start_coordinates]

#print(f'stops_coordinates = {stops_coordinates} \n start_coordinates = {start_coordinates}')
#print(f'{matrix} \n matrix_len = {matrix_len} \n matrix_height = {matrix_height}')

direction = ['N','E','S','W']
current_direction = 'N'
current_position = start_coordinates

def change_direction(current_direction):
    if current_direction != 'W':
        current_direction = direction[direction.index(current_direction) + 1]
    else:
        current_direction = 'N'

    move(current_direction)

    return current_direction


visited_coordinates = stops_coordinates + [start_coordinates.copy()]

def move(current_direction):
    global step_counter
    if current_direction == 'N':
        while True:
            current_position[1] -= 1
            if current_position not in visited_coordinates:
                visited_coordinates.append(current_position.copy())
                step_counter += 1
                print(f'N , {step_counter}')
            if current_position in stops_coordinates:
                current_position[1] += 1
                change_direction('N')

                break

            elif current_position[1] == 0:
                print(f'final N, {step_counter}')
                
                break

    elif current_direction == 'E':
        while True:
            current_position[0] += 1
            if current_position not in visited_coordinates:
                visited_coordinates.append(current_position.copy())
                step_counter += 1
                print(f'E , {step_counter}')
            if current_position in stops_coordinates:
                current_position[0] -= 1
                change_direction('E')

                break

            elif current_position[0] == matrix_len - 1:
                print(f'final E, {step_counter}')

                break

    elif current_direction == 'S':
        while True:
            current_position[1] += 1
            if current_position not in visited_coordinates:
                visited_coordinates.append(current_position.copy())
                step_counter += 1
                print(f'S , {step_counter}')
            if current_position in stops_coordinates:
                current_position[1] -= 1
                change_direction('S')

                break

            elif current_position[1] == matrix_height - 1:
                print(f'final S, {step_counter}')

                break

    elif current_direction == 'W':
        while True:
            current_position[0] -= 1
            print(f'current_position {current_position}')
            if current_position not in visited_coordinates:
                visited_coordinates.append(current_position.copy())
                step_counter += 1
            if current_position in stops_coordinates:
                current_position[0] += 1
                change_direction('W')

                break

            elif current_position[0] == 0:
                print(f'final W, {step_counter}')

                break


move(current_direction)