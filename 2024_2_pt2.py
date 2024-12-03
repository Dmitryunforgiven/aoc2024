from puzzle_input_2 import input

reports_list = input.split('\n')
reports = [[int(i) for i in report.split()] for report in reports_list]

def is_safe(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        diff = [abs(i - j) for i, j in zip(report, report[1:])]
        if all(1 <= x <= 3 for x in diff):
            return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if modified_report == sorted(modified_report) or modified_report == sorted(modified_report, reverse=True):
            diff = [abs(i - j) for i, j in zip(modified_report, modified_report[1:])]
            if all(1 <= x <= 3 for x in diff):
                return True

    return False

counter = sum(1 for report in reports if is_safe(report))

print(counter)