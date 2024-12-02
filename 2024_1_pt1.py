from puzzle_input_1 import input

separated_list = [item for sub in input.split('\n') for item in sub.split('   ')]
even_list = separated_list[0::2]
uneven_list = separated_list[1::2]

counter = sum(abs(int(left) - int(right)) for left, right in zip(sorted(even_list), sorted(uneven_list)))   
print(counter)