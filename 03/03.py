# Each row must be ONLY decreasing or increasing,
# and must increase or decrease by at least 1, and not more than 3
from aocd import get_data
from re import findall as findall
from re import search as search

# Import puzzle data and print to terminal
data = get_data(day=3, year=2024)

# Part 1
p1_mem_regex = "mul\(\d{1,3},\d{1,3}\)"
p1_operations = findall(p1_mem_regex, data)
p1_calcs = []

# Manipulate list to remove "mul()" and then multiply the numbers and append to a list to be summed at the end
for idx, operation in enumerate(p1_operations):
    p1_operations[idx] = findall("\d{1,3},\d{1,3}", operation)[0]
    p1_calcs.append(int(p1_operations[idx].split(",")[0]) * int(p1_operations[idx].split(",")[1]))

# Print result
print(sum(p1_calcs))

# Part 2
# regex also checks for do() and don't() in order to update the mul_enabled flag
p2_mem_regex = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
p2_operations = findall(p2_mem_regex, data)
p2_calcs = []
# Default to enabled as per puzzle
mul_enabled = 1

# Enumerate list, if operation matches do() or don't() then update mul_enabled flag and continue.
# If set to 1 then add result to p2_calcs list to sum later, otherwise do not and continue looping
for idx, p2_operation in enumerate(p2_operations):
    if p2_operations[idx] != "do()" and p2_operations[idx] != "don't()":
        p2_operations[idx] = findall("\d{1,3},\d{1,3}", p2_operation)[0]
    if p2_operations[idx] == "do()":
        mul_enabled = 1
    elif p2_operations[idx] == "don't()":
        mul_enabled = 0
    elif mul_enabled == 1:
        p2_calcs.append(int(p2_operations[idx].split(",")[0]) * int(p2_operations[idx].split(",")[1]))
    elif mul_enabled == 0:
        print("MUL disabled, not checking")

print(sum(p2_calcs))