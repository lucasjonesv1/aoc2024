# Each row must be ONLY decreasing or increasing,
# and must increase or decrease by at least 1, and not more than 3
from aocd import get_data
from re import findall as findall
from re import search as search

# Import puzzle data and print to terminal
data = get_data(day=3, year=2024)

mem_regex = "mul\(\d{1,3},\d{1,3}\)"

operations = findall(mem_regex, data)
calcs = []

for idx, operation in enumerate(operations):
    operations[idx] = findall("\d{1,3},\d{1,3}", operation)[0]
    calcs.append(int(operations[idx].split(",")[0]) * int(operations[idx].split(",")[1]))

print(sum(calcs))