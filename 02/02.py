# Each row must be ONLY decreasing or increasing,
# and must increase or decrease by at least 1, and not more than 3
from aocd import get_data

# Import puzzle data and print to terminal
data = get_data(day=2, year=2024)

str_reactor_reports = data.split('\n')
reactor_reports = []
# Convert string lists to int lists
for str_report in str_reactor_reports:
    report = [int(item) for item in str_report.split(' ')]
    reactor_reports.append(report)

unsafe_reports = 0
safe_reports = 0

# For each report, enumerate the reports and check if next index is larger or smaller
for each in reactor_reports:
    increasing = 0
    decreasing = 0
    unstable = 0
    # loop through report, using [:-1] to avoid index out of bounds error
    for idx, x in enumerate(each[:-1]):
        if x > each[idx+1] and x % each[idx+1] < 4 and x % each[idx+1] != 0:
            decreasing += 1
        elif x < each[idx+1] and each[idx+1] % x < 4 and each[idx+1] % x != 0:
            increasing += 1
        else:
            unstable += 1

    if increasing <= 1 and decreasing == len(each[:-2]):
        print("decreasing only within tolerance: " + str(each))
        safe_reports += 1
    elif decreasing <= 1 and increasing == len(each[:-2]):
        print("increasing only within tolerance: " + str(each))
        safe_reports += 1
    elif increasing == len(each[:-1]):
        print("increasing only: " + str(each))
        safe_reports += 1
    elif decreasing == len(each[:-1]):
        print("decreasing only: " + str(each))
        safe_reports += 1
    elif unstable > 0:
        print("unstable: " + str(each))
        unsafe_reports += 1
    
print(safe_reports)