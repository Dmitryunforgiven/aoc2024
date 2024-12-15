from puzzle_input_5 import input
from test import test_input


row = input.split('\n')

rule_list = [i for i in row if '|' in i and i.strip()]
rule_list = [i.split('|') for i in rule_list]
e_list = [i.split(',') for i in row if '|' not in i and i.strip()]

def check_order(sublist, rule_list):
    for rule in rule_list:
        first, second = rule
        if first in sublist and second in sublist:
            if sublist.index(first) > sublist.index(second):
                return False
    return True

result = 0

for sublist in e_list:
    if check_order(sublist, rule_list):
        result += int(sublist[len(sublist) // 2])

print(result)