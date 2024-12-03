from puzzle_input_3 import input
import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
match = [list(i) for i in (re.findall(pattern, input))]


x = sum(int(i[0]) * int(i[-1]) for i in match)

print(x)