from puzzle_input_2 import input


reports_list = input.split('\n')
#report = [i for reports_list in input.split('\n') for i in reports_list.split(' ')]
reports = [[int(i) for i in report.split()] for report in reports_list]
counter = 0

def is_safe(report):
    dec = report == sorted(report, reverse=True)
    inc = report == sorted(report)
    if not (dec or inc):
        return False
    
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

for report in reports:
    if is_safe(report):
        counter += 1    

print(counter)