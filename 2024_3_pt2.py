import re
from puzzle_input_3 import input

main_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
i_pattern = r"\d{1,3}"

matches = re.findall(main_pattern, input)

is_relevant = True
result = 0

for i in matches:
    if i == "don't()":
        is_relevant = False
    elif i == "do()":
        is_relevant = True

    if i.startswith("mul") and is_relevant:
        numbers =[int(j) for j in (re.findall(i_pattern, i))]
        result += numbers[0] * numbers[1]
    
print(result)