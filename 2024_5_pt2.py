from puzzle_input_5 import input
from test import test_input

row = input.strip().split('\n')

rule_list = [i for i in row if '|' in i and i.strip()]
rule_list = [i.split('|') for i in rule_list]
e_list = [i.split(',') for i in row if '|' not in i and i.strip()]

def check_order(sublist, rule_list):

    changed = False
    while True:
        sublist_copy = sublist[:]
        for rule in rule_list:
            first, second = map(str.strip, rule)
            if first in sublist_copy and second in sublist_copy:
                if sublist_copy.index(first) > sublist_copy.index(second):
                    sublist_copy.remove(second)
                    sublist_copy.insert(sublist_copy.index(first) + 1, second)
                    changed = True
        if sublist_copy == sublist:
            break
        sublist[:] = sublist_copy
    return changed

result = 0

for sublist in e_list:
    if check_order(sublist, rule_list):
        if sublist:
            middle_value = int(sublist[len(sublist) // 2])
            result += middle_value

print(result)