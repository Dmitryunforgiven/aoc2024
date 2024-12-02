from puzzle_input_1 import input

separated_list = [item for sub in input.split('\n') for item in sub.split('   ')]
even_list = separated_list[0::2]
uneven_list = separated_list[1::2]

counter = sum(int(i) * uneven_list.count(i) for i in even_list)
print(counter)